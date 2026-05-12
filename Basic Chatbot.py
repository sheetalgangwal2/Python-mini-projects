print("Hy, It's mini chatbot")

user = input("Enter something: ").lower()


while user != "exit":
    if(user == "hi"):
        print("Hello!\nHope you are doing well!")
    elif(user == "how are you"):
        print("I am fine , thanks")
    elif(user == "bye"):
        print("Goodbye\nHave a nice day!")
    else:
        print("feel free to say ")
    print()
    user = input("Enter text: ").lower()

print("Chatbot closed.")

