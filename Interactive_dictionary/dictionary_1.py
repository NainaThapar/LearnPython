import json
import difflib
from difflib import get_close_matches

#Loading json data as python dictionary
data = json.load(open("dictionary.json"))

#Function for retrieving definition
def retrieve_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word_user, data.keys())) > 0:
        action = input('Did you mean %s instead? [y or n]:' %get_close_matches(word_user, data.keys())[0])
        if(action == 'y'):
            return data[get_close_matches(word,data.keys())[0]]
        elif(action == 'n'):
            return "The word doen't exist, yet"
        else:
            return "We don't understand your entry. Apologies!"
    else:
        return("The word doesn't exist, please double check it")

#Input from user
word_user = input("Enter a word : ")

#Retrieve definition using function and print the result
output = retrieve_definition(word_user)

if type(output) == list:
    for item in output:
        print('-',item)
else:
    print('-',output)
