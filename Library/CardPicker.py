from Library import helpers, config
from Library.crypto import private_key, public_key, hashing


class CardPicker:

    def __init__(self, websocket):
        self.name = config.card_picker_name
        self.cards = config.cards
        self.guesser_name = config.card_guesser_name
        self.password = private_key.generate_password()
        self.private_key = private_key.generate_private_key_pem_string(self.password)
        self.public_key = public_key.generate_public_key_pem_string(self.private_key, self.password)
        self.websocket = websocket

    async def start_game(self):
        handshake = await self.receive()
        handshake = helpers.load_json(handshake)
        guesser_public_key = handshake["public_key"]
        card = helpers.choose_card(self.cards, "Pick a card")
        card = self.cards[card]
        signature = private_key.sign(
            private_key_pem_string=self.private_key,
            password=self.password,
            message=card
        )
        message = {
            "message": "I've chosen my card, I have revealed the hash of my signature so you can validate my honesty",
            "signature_hash": hashing.hash(signature)
        }
        await self.send(helpers.get_json(message))
        print("{0} is guessing a card...".format(self.guesser_name))
        received_message_json = await self.receive()
        received_message = helpers.load_json(received_message_json)
        signature_is_valid = public_key.verify_signature(
            public_key_pem_string=guesser_public_key,
            signature=received_message["signature"],
            message=received_message["guessed_card"]
        )
        if signature_is_valid:
            card_picked = helpers.choose_card(self.cards, "What card do you want to reveal?")
            card = self.cards[card_picked]
            message = {
                "message": "The Card I have chosen is: {0}".format(card),
                "card": card,
                "public_key": self.public_key,
                "signature": signature
            }
            await self.send(helpers.get_json(message))
            confirmation_message = await self.receive()
            confirmation_message = helpers.load_json(confirmation_message)
            if confirmation_message['message']:
                if card == received_message["guessed_card"]:
                    print("{0} Wins!".format(self.guesser_name))
                else:
                    print("{0} Wins!".format(self.name))
            else:
                print("{0} is not Honest :(, {1} Wins!".format(self.name, self.guesser_name))
        else:
            await self.send(helpers.get_json({'message': False}))
            print("{0} is not Honest :( {1} Wins!".format(self.guesser_name, self.name))

    async def send(self, msg):
        await self.websocket.send(msg)
        print("{0} => {1}: {2}".format(self.name, self.guesser_name, msg))

    async def receive(self):
        msg = await self.websocket.recv()
        print("{0} => {1}: {2}".format(self.guesser_name, self.name, msg))
        return msg
