#!/us/bin/env python3

"""Create a function called words_with_vowels, this function
takes a string of words and returns a list of only words that have
vowels in them. For example, 'You have no rhythm' should
return ['You','have', 'no']."""


def word_with_vowels(string_of_words: str) -> list:
    return [
        word for word in string_of_words.split()
        if 'a' in word or 'e' in word or 'i' in word or 'o' in word
        or 'u' in word
    ]


"""
Extra Challenge: Class of Cars
b. Create three classes of three car brands – Ford, BMW, and
Tesla. The attributes of the car's objects will be, model,
color, year, transmission, and whether the car is
electric or not (Boolean value.) Consider using inheritance
in your answer.
You will create one object for each car brand:
bmw1 : model: x6, Color: silver, Year: 2018, Transmission: Auto, Electric: False
tesla1: model: S, Color: beige, Year: 2017, Transmission: Auto, Electric: True
ford1 : model: focus, Color: white, Year: 2020, Transmission: Auto, Electric: False
You will create a class method, called print_cars that will be
able to print out objects of the class. For example, if you call the
method on the ford1 object of the Ford class, your function
should be able to print out car info in this exact format:
car_model = focus
Color = White
Year = 2020
Transmission = Auto
Electric = False"""


class Car:
    def __init__(self, model, color, year, transmission, is_electric):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.is_electric = is_electric

    def __str__(self):
        return f"car_model = {self.model}\nColor = {self.color}\nYear = {self.year}\nTransmission = {self.transmission}\nElectric = {self.is_electric}"


class Ford(Car):
    pass


class BMW(Car):
    pass


class Tesla(Car):
    pass


bmw1 = BMW("x6", "silver", 2018, "Auto", False)
tesla1 = Tesla("S", "beige", 2017, "Auto", True)
ford1 = Ford("focus", "white", 2020, "Auto", False)


def print_cars(car):
    print(car)


print(word_with_vowels("You have no rhthym"))
print_cars(tesla1)
