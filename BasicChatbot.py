#Basic ChatBot implementation that anser Baisc python questions

def getmessage(message):

    #messages for greetings
    if("hello" in message):
        reply="Hi!"
    
    elif("how are you" in message):
        reply="I'm Fine,thanks!"

    elif("thank you" in message):
            reply="your're Welcome!"

    elif( "what is your name" in message):
        reply="I am a basic chatbot."

    elif("what can you do" in message):
        reply="I can answer some basic python questions"

    elif("who created you" in message):
        reply="An intern created me using python."




    # Answer basic Python questions
    elif("what is python" in message):
        reply="python is high-level-programming language"
    
    elif("creator of python" in message):
        reply="Python was created by Guido van Rossum."
    
    #what is a variable?
    elif("variable" in message): 
        reply=" A variable is used to store a value."

    elif("where python is used" in message):
        reply="Python is used for web development, data science, automation, AI, and more."

    #what is an interpreter
    elif("interpreter" in message):
        reply="An interpreter executes Python code."

    #any questions related to datatypes
    elif("datatypes" in message):
        reply = "Common Python data types are int, float, string, list, tuple, set and dictionary."

    
    elif("integer" in message): #what is an integer
        reply = "An integer is a whole number, such as 10 or -5."

    elif("float" in message): #what is a float
        reply = "A float is a number with a decimal point, such as 3.14."

    elif("string" in message): #what is a string
        reply = "A string is a sequence of characters."

    elif("list" in message): #what is a list
        reply = "A list is an ordered and changeable collection of items."

    elif("tuple" in message): #what is a list
        reply = "A tuple is an ordered collection that cannot be changed."

    elif("dictionary" in message): #what is a dictionary in python
        reply = "A dictionary stores data in key-value pairs."

    elif("set" in message): #what is a set in python
        reply = "A set is an unordered collection of unique items."

    elif("function" in message): #what is a function in python
        reply = "A function is a reusable block of code."

    elif("loop" in message): #what is a loop in python
        reply = "A loop is used to repeat a block of code."
 
    elif("for loop" in message): #what is a for loop in python
        reply = "A for loop is used to iterate over a sequence."

    elif("while loop" in message): #what is a while loop in python
        reply = "A while loop repeats code while a condition is true."

    elif("if else" in message):
        reply = "If-else is used to make decisions in a program."


    elif("print()" in message): #why print() used in python
        reply = "print() is used to display output."

        
    elif("input()" in message): #why input() is used in python
        reply = "input() is used to take input from the user."

    elif("len()" in message): #why len() is used in python
        reply = "len() is used to find the length of an object."

    elif("break" in message): #why break used in python
        reply = "break is used to stop a loop."

    elif("continue" in message): #why continue used in python
        reply = "continue skips the current iteration and continues the loop."



    #end the converstion
    elif("bye" in message):
        reply="GoodBye"

    ##default reply is send if question is not known
    else:
        reply="I'm sorry,I don't understand"

    #returns the reply to bot_reply variable
    return reply


#diplay welcome message 
print("Hello,How can i help you\n")

#it repeats until user end the conversation
while True:

    #take input from the user
    user_message=input("Human:").lower()

    #get reply for user message from getmessage() function
    bot_reply=getmessage(user_message)

    #display the response
    print("Bot:",bot_reply)

    #chatbot terminates if user enter "bye" message
    if("bye" in user_message):
        break



