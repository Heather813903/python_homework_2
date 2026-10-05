# Task 1

def hello():
    return "Hello!"

print (hello())

#Task 2

def greet (name):
    return (f"Hello, {name}!")

print ("James")

#Task 3

def calc (a, b, operation="multiply"):
    try:
        if operation == "multiply":
            return a * b
        elif operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"


#Task 4


def data_type_conversion(value, name):
    try:
        if name == "float":
            return float(value)
        elif name == "str":
            return str(value)
        elif name == "int":
            return int(value)
    except ValueError:
        return f"You can't convert {value} into a {name}."

#Task 5

def grade (*args):
    try:        
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60: 
            return "D"
        else:
            return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."

#Task 6

def repeat (string, count):
    result = ""
    for i in range(count):
        result += string
    return result


#Task 7

def student_scores (operation, **kwargs):
    if operation == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif operation == "best":
        highest_score = 0
        best_student = ""
        for key, value in kwargs.items():
            if value > highest_score:
                highest_score = value
                best_student = key
        return best_student


#Task 8

def titleize (string):
    words = string.split()
    for i, word in enumerate(words):
        if i == 0:
            words[i] = word.capitalize()
        elif i ==len(words) -1:
            words[i] = word.capitalize()
        elif word not in ("a", "on", "an", "the", "of", "and", "is", "in"):
            words[i] = word.capitalize()
    return" ".join(words)

#Task 9

def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result

#Task 10



def pig_latin(string):
    words = string.split()
    result = ""

    for word in words:
        if word[0] in "aeiou":
            result += word + "ay" + " "
        else:
            i = 0

            while i < len(word) and word[i] not in "aeiou":
                i += 1

            if word[i-1:i+1] == "qu":
                i += 1

            result += word[i:] + word[:i] + "ay" + " "

    return result.strip()