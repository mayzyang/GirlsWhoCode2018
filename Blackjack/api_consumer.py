import requests

API_BASE_URL = "http://deckofcardsapi.com/api"

# This function should shuffle a deck and return a deck_id from the Deck of Cards API
def shuffle():

    # TODO: Make HTTP request here to shuffle a new deck
    request = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    json_parsed_data = request.json()

    # TODO: if this was a successful request ...:
    if request.status_code == 200 and json_parsed_data["success"] == True:
        return json_parsed_data["deck_id"]
    else:
        raise Exception("Trouble shuffling the deck!")
        return 0
    # else:
# This function should call the Deck of Cards API
def draw_cards(deck_id, number_of_cards):

    # TODO: Make HTTP request here to draw {number_of_cards} cards from deck with id {deck_id}
    url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=" + str(number_of_cards)
    cards = requests.get(url)

    if cards.status_code == 200:
        return cards.json().get("cards")
    else:
        raise Exception("Error drawing cards (greasy fingers maybe)!")
