from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_one_joke():
    return choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)
#print(get_one_joke())

def get_jokes(n):
     jokes = []
     for i in range(n):
        get_one_joke()
        jokes.append(get_one_joke())
     print(jokes)
get_jokes(4)



