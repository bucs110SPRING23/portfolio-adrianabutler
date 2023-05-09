import requests
import json

class RandomJoke:
    """
    Fetches random joke from Random Joke API
    """
    def __init__(self):
        """
        Initializes class
        Sets URL to variable for driver code
        """
        self.joke_url = "https://api.joke.one" 

    def random_joke(self):
        """
        Fetches random joke 
        Prints random joke and if unable to, prints none was found
        """
        response = requests.get(RandomJoke().joke_url)
        data = response.json()

        if "setup" in data and "punchline" in data:
            setup = data["setup"]
            punchline = data["punchline"]
            print("Joke:")
            print(setup)
            print(punchline)
        else:
            print("No joke found.")