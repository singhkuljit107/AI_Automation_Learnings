import requests
import random


def get_random_products():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        joke_data = data["data"]
        joke = joke_data["content"]

        return joke
    else:
        raise Exception("Failed to fectch joke data")


def main():
    try:
        joke = get_random_products()
        print(
            f"Joke: {joke} ")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
