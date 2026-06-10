from datetime import datetime
import random
quotes = [
    "Success comes from consistency.",
    "Keep learning and growing.",
    "Every expert was once a beginner."
]
print("=== SMART CHATBOT ===")
while True:
    user = input("You: ").lower()
    if user == "hello":
        print("Bot: Hello! Nice to meet you.")
    elif user == "time":
        print("Bot:", datetime.now().strftime("%H:%M:%S"))
    elif user == "date":
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))
    elif user == "quote":
        print("Bot:", random.choice(quotes))
    elif user == "calculator":
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+,-,*,/): ")
        num2 = float(input("Enter second number: "))
        if op == "+":
            print("Result =", num1 + num2)
        elif op == "-":
            print("Result =", num1 - num2)
        elif op == "*":
            print("Result =", num1 * num2)
        elif op == "/":
            print("Result =", num1 / num2)

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I don't understand.")