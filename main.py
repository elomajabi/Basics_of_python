# Task 1 - Make a program that asks for names. If the name is on our VIP list, they get in. If not, they are rejected. We will use a loop so the program keeps running until we type “exit”

vip_names = ["wojtek" , "norbert" , "kalina" , "maja" , "piotrek"]
bad_names = ["kot" , "kotek" , "nikola" , "dziewczyna norberta" , "kocur" , "ignas" , "ignacy"]

while True:
    name = input("What is your name? ")

    if name.lower() == "exit":
        print("Goodbye!")
        break

    if name.lower() in vip_names:
        print(f"Welcome to VIP, {name}")

    elif name.lower() in bad_names:
        print(f"You are not invited, {name}")

    else:
        print(f"Go to kwadratowa {name}")
