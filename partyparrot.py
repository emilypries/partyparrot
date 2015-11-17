<<<<<<< HEAD
import sys
import random

ALPHABET = {
    'a': [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'b': [
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,0],
    ],
    'c': [
        [0,1,1,1,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [0,1,1,1,1],
    ],
    'd': [
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,0],
    ],
    'e': [
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,1],
    ],
    'f': [
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
    ],
    'g': [
        [0,1,1,1,1],
        [1,0,0,0,0],
        [1,0,1,1,1],
        [1,0,0,0,1],
        [0,1,1,1,1],
    ],
    'h': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'i': [
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
    ],
    'j': [
        [0,0,1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    'k': [
        [1,0,0,1,0],
        [1,0,1,0,0],
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'l': [
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,1],
    ],
    'm': [
        [1,0,0,0,1],
        [1,1,0,1,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    'n': [
        [1,1,0,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,0,1,1],
    ],
    'o': [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    'p': [
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
    ],
    'q': [
        [0,1,1,0,0],
        [1,0,0,1,0],
        [1,0,0,1,0],
        [1,0,0,1,0],
        [0,1,1,1,1],
    ],
    'r': [
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,0,1,0],
        [1,0,0,0,1],
    ],
    's': [
        [0,1,1,1,1],
        [1,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,1],
        [1,1,1,1,0],
    ],
    't': [
        [1,1,1,1,1],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
    ],
    'u': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    'v': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [0,0,1,0,0],
    ],
    'w': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,1,0,1,1],
        [1,0,0,0,1],
    ],
    'x': [
        [1,0,0,0,1],
        [0,1,0,1,0],
        [0,0,1,0,0],
        [0,1,0,1,0],
        [1,0,0,0,1],
    ],
    'y': [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
    ],
    'z': [
        [1,1,1,1,1],
        [0,0,0,0,1],
        [0,1,1,1,0],
        [1,0,0,0,0],
        [1,1,1,1,1],
    ]
}
=======
import json
import requests
import argparse
import itertools
import os
from alphabet import ALPHABET
>>>>>>> d9da5651857c2d37063ec4063041b494e6d1724a

PARTY_PARROTS = [
    ':partyparrot:',
    ':partyparrot2:',
    ':partyparrot3:',
    ':partyparrot4:'
]


def arr_to_str(c, s, space):
    if c == ' ':
        return '\n\n\n\n\n\n\n\n'
    arr = ALPHABET[c]
    output_string = ''
    for row in arr:
        for col in row:
            output_string += s if col else space
        output_string += '\n'

    return output_string


<<<<<<< HEAD
def convert_str_to_emoji(s, emojis=PARTY_PARROTS):
=======
def post_text_to_slack(output_string):
    if 'SHITPOSTING_ENDPOINT' not in os.environ:
        print('SHITPOSTING_ENDPOINT is not in your environment. Fix that.')
        return

    payload = {
        'username': 'The Party Parrot',
        'icon_emoji': ':partyparrot:',
        'text': output_string
    }

    return requests.post(os.environ['SHITPOSTING_ENDPOINT'], data=json.dumps(payload))


def convert_str_to_emoji(s, emojis=PARTY_PARROTS, space=' ', force=False):

    emoji_iterator = itertools.cycle(emojis)

>>>>>>> d9da5651857c2d37063ec4063041b494e6d1724a
    s = s.lower()
    output_string = ''
    for c in s:
        output_string += arr_to_str(c, emoji_iterator.next(), space)
        output_string += '\n\n'
    return output_string

if __name__ == '__main__':
<<<<<<< HEAD
    input_str = sys.argv[1]
    if len(sys.argv) > 2:
        emojis = sys.argv[2:]
        print convert_str_to_emoji(input_str, emojis=emojis)
    else:
        print convert_str_to_emoji(input_str)
=======
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='The text to emoji-fy')
    parser.add_argument('-e', '--emojis', nargs='+', help='List of emojis to use.', default=PARTY_PARROTS)
    parser.add_argument('-f', '--force', action='store_true', help='automatically post to the slack of your choosing', default=False)
    parser.add_argument('-s', '--space', default='        ')

    args = parser.parse_args()

    out_str = convert_str_to_emoji(args.text,
                                   emojis=args.emojis,
                                   space=args.space,
                                   force=args.force
                                   )
    print(out_str)
>>>>>>> d9da5651857c2d37063ec4063041b494e6d1724a
