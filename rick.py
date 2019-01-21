import requests
import argparse
import re
import sys
import random


leetascii = """
      _      _              _ _ _                 
 _ __(_) ___| | ___ __ ___ | | | | ___   __ _ ___ 
| '__| |/ __| |/ / '__/ _ \| | | |/ _ \ / _` / __|
| |  | | (__|   <| | | (_) | | | | (_) | (_| \__ \\
|_|  |_|\___|_|\_\_|  \___/|_|_|_|\___/ \__, |___/
 @hacker_                                |___/                               
"""


def url(s):
    s = re.sub("\s+", "+", s)
    s = '/'+s
    return s


parser = argparse.ArgumentParser()
parser.add_argument('-d', dest='domain', required=True)
args = parser.parse_args()
d = args.domain
meme = ["┏(・o･)┛", "┗(・o･)┓"]
print(leetascii)
sys.stdout.write("rick rolling! ")


def rickroll():
    if(d.startswith('http://') or d.startswith('https://')):
        with open('lyrics.txt', 'r') as lyrics:
            for line in lyrics:
                target = args.domain+url(line)
                requests.get(target, headers={"User-Agent": "rickrolllogs"})
                sys.stdout.write(random.choice(meme))
                sys.stdout.flush()
                sys.stdout.write("\b\b\b\b\b\b\b\b")
        print("\n\ndoneᕕ( ᐛ )ᕗ")
    else:
        print("error: invalid domain specified")


try:
    rickroll()
except KeyboardInterrupt:
    print("exiting.")
