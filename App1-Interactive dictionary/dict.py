import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        print("Definition:-\n")
        return data[w]
    elif len(get_close_matches(w,data.keys(),cutoff=0.7)) > 0:
        yn=input( "Did you mean %s instead? press Y for yes or N for No: " %get_close_matches(w,data.keys())[0])
        if yn=="Y":
            print( "Definition:-\n")
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return "the word entered doesn't exist.please check it!"
        else:
            return "The input is Invalid"
    else:
        return "The word entered doesn't exist. please check it!"
word= input("Enter your query: \n")

output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
