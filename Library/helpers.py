import json


def load_json(msg_json):
    return json.loads(msg_json)


def get_json(msg_dict):
    return json.dumps(msg_dict)


def choose_card(cards, msg):
    while True:
        val = input("{0} cards:{1} (please enter a number from 0 to {2}): ".format(msg, cards, len(cards) - 1))
        try:
            val = int(val)
        except ValueError:
            continue
        if val in range(0, len(cards)):
            return val