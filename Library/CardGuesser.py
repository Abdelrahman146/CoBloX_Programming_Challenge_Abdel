from Library import helpers, config
from Library.crypto import private_key, public_key, hashing


class CardGuesser:

    def __init__(self, websocket):
        self.websocket = websocket
        self.name = config.card_guesser_name
        self.picker_name = config.card_picker_name
        self.cards = config.cards
        self.password = private_key.generate_password()
        self.private_key = private_key.generate_private_key_pem_string(self.password)
        self.public_key = public_key.generate_public_key_pem_string(self.private_key, self.password)

    async def start_game(self):
        await self.send(helpers.get_json({"message": "I am {0}, please receive my public_key".format(self.name), "name":self.name, "public_key": self.public_key}))
        print("{0} is picking a card...".format(self.picker_name))
        received_message = await self.receive()
        received_message = helpers.load_json(received_message)
        received_signature_hash = received_message["signature_hash"]
        guessed_card = helpers.choose_card(self.cards, "Guess what is the card that {0} has picked".format(self.picker_name))
        guessed_card = self.cards[guessed_card]
        signature = private_key.sign(
            private_key_pem_string=self.private_key,
            password=self.password,
            message=guessed_card
        )
        message = {
            "message": "I guess the card is {0}".format(guessed_card),
            "guessed_card": guessed_card,
            "signature": signature
        }
        await self.send(helpers.get_json(message))
        print("{0} is asking you to wait :) ...".format(self.picker_name))
        confirmation_message = await self.receive()
        received_message = helpers.load_json(confirmation_message)
        if received_message["message"]:
            signature_is_valid = public_key.verify_signature(
                public_key_pem_string=received_message["public_key"],
                signature=received_message["signature"],
                message=received_message["card"]
            )
            signature_hash_match = hashing.hash(received_message["signature"]) == received_signature_hash
            if signature_is_valid and signature_hash_match:
                await self.send(helpers.get_json({"message": True}))
                if guessed_card == received_message["card"]:
                    print("{0} Wins!".format(self.name))
                else:
                    print("{0} Wins!".format(self.picker_name))
            else:
                await self.send(helpers.get_json({"message": False}))
                print("{0} is not honest :(, {1} Wins!".format(self.picker_name, self.name))
        else:
            print("{0} is not honest :( {1} Wins!".format(self.name, self.picker_name))

    async def send(self, msg):
        await self.websocket.send(msg)
        print("{0} => {1}: {2}".format(self.name, self.picker_name, msg))

    async def receive(self):
        msg = await self.websocket.recv()
        print("{0} => {1}: {2}".format(self.picker_name, self.name, msg))
        return msg

