import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(

    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )

cursor = con.cursor()

word = input("Enter word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()
print(results)
data = dict(results)

def translate(w):
    w = w.lower()
    if w in data: 
        return data[w]
        """
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else: 
            return "We didn't understand your entry."
            """

    else:
        return "The word doesn't exist. Please double check it."


output = translate(word)

#if type(output) == list:
 #   for item in output:
  #      print(item)
#else:
print(output)  



