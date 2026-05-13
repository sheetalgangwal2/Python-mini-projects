print("WELCOME!")

user = input("Enter movie genre (comedy, action, horror, adventure, romantic) : ").lower()
while user != "exit":
    if(user == "comedy"): 
        print({"Welcome", "Hera-Pheri", "Dhamaal", "Golmaal", "Chhichhore"})
    elif(user == "adventure"):
       print({"Avtaar", "Interstellar", "Jumanji", "Uncharted", "Everest"})
    elif(user == "action"):
        print({"Pushpa", "Dhurandhar", "KGF", "Gadar 2", "Chhava"})
    elif(user == "romantic"):
        print({"DDLJ", "Dhadak", "Barfi", "Sita Ramam", "Love aaj kal"})
    elif(user == "horror"):
        print({"Stree", "Bhool bhulaiya", "Munjya", "Shaitaan", "Tumbbad"})
    else:
        print("Invalid type! Try again......")
    print()
    user = input("Enter movie genre : ").lower()