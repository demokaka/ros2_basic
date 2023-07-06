import requests


def randomquotes():
    # Make a request to the API
    response = requests.get("https://zenquotes.io/api/random")

    # Parse the JSON response
    data = response.json()

    # Get the random quote and author
    quote = data[0]['q']
    author = data[0]['a']

    # Print the random quote
    res_quote = f"{quote} - {author}"
    return res_quote

print(randomquotes())