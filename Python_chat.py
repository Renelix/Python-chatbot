
# Inclusione delle librerie.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import levenshtein_distance
from chatterbot.response_selection import get_first_response
import logging

logging.basicConfig(level=logging.CRITICAL)


# Inizializzazione dell'oggetto Bot di tipologia ChatBot.

Bot = ChatBot(
    "James",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="./db.sqlite3",
    logic_adapters=["chatterbot.logic.BestMatch"],
    statement_comparison_function=levenshtein_distance,
    response_selection_method=get_first_response
)


# Apertura file con dizionario base di parole, per l'allenamento del Bot.

with open("C:/Users/Antonio/Desktop/Parole.txt") as f:
    Conversazione = f.readlines()
    Allenamento = ListTrainer(Bot)
    Allenamento.train(Conversazione)


# Ciclo infinito che crea tutta la chat.

while True:
    try:
        Nome_user = input("Tu: ")
        Risposta_bot = Bot.get_response(Nome_user)
        print("Bot: ", Risposta_bot)
    except(KeyboardInterrupt, EOFError, SystemExit):
        print("Ciao.")
        break
