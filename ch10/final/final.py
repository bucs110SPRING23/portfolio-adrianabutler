import requests
import json
from jokes import RandomJoke
from random_emoji import EmojiAPI

def main():
    RandomJoke.random_joke()
    EmojiAPI.random_emoji()

main()