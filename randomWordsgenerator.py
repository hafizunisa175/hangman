import random
from randomwords import list_of_words
def getWord():
    global word
    word=random.choice(list_of_words).upper()
