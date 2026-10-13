print("Hello, I am Roko AI agent What can i help you?")

conversation = []

salutation = input("Enter how can i refer to you: ").lower()




while True:
    user_text = input("You: ").lower()

    if user_text == "quit":
        break

    conversation.append({"role": "user", "content": user_text})

    if "hello" in user_text or "hi" in user_text:
        reply = f"Hello, I am your new ai agent. What can i do for you {salutation}?" 
    
    elif "name" in user_text:
        reply = "My name is Roko the AI agent. Whats yours?"
    elif "age" in user_text:
        reply = "I am created for your humble assistant."
    elif "price" in user_text:
        reply = "if i am you most lovable and caring assistant then i am priceless"
    elif "history" in user_text or "replay" in user_text:
        for text in conversation:
            print(text["role"], ":", text["content"])
        continue

    else:
        reply = "I don't know yet. Can you teach me or add some rules."

    conversation.append({"role": "Bot", "content": reply})
    print("Bot:", reply)

  
 
print(f"Good bye {salutation}")
