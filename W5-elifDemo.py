# elif is different from if, because as soon as one statement is true, it will SKIP the remainder of the statements.
answer = input("What do you think about 4chan?")
if len(answer) > 200:
    print("wow, you had a lot to say about that")
elif len(answer) > 125:
    print("I didn't know you thought about it that much")
elif len(answer) > 50:
    print("I guess that is about right")
elif len(answer) > 1:
    print ("Hello?")
else:
    print("Dont want to talk about it huh?")
print("Lets talk about something else then.")