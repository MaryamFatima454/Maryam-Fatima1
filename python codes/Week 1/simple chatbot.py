print("Hello! I'm ChatBot. How can I help you today?")
user_input = input("You: ").lower()
if "hello" in user_input or "hi" in user_input:
    print("ChatBot: Hello there! ")
elif "how are you" in user_input:
    print("ChatBot: I'm just a program, but I'm doing great!")
elif "your name" in user_input:
    print("ChatBot: I'm a simple chatbot made with Python.")
elif "bye" in user_input:
    print("ChatBot: Goodbye! Have a nice day! ")
else:
    print("ChatBot: Sorry, I didn't understand that.")
