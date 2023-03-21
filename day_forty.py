#!/usr/bin/python3

from collections import deque


"""Write a function called translate that takes the following
words and translates them into pig Latin.
a = 'i love python'
Here are the rules:
1. If a word starts with a vowel (a,e, i, o, u) add 'yay' at the
end. For example, 'eat' will become 'eatyay'
2. If a word starts with anything other than a vowel, move
the first letter to the end and add 'ay' to the end. For
example, 'day' will become 'ayday'.
Your code should return:
iyay ovelay ythonpa"""


def translate(stringInEnglish: str) -> str:
    wordList = stringInEnglish.lower().split(" ")
    pigLatinWordList = []
    for word in wordList:
        if word.startswith(("a", "e", "i", "o", "u")):
            word += "yay"
            pigLatinWordList.append(word)
        else:
            wordDeque = deque(word)
            wordDeque.rotate(-1)
            wordDeque.append("ay")
            pigLatinWordList.append("".join(wordDeque))

    return " ".join(pigLatinWordList)


print(translate("I love python"))
