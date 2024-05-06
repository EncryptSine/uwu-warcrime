import random

def modify_input(input_text):
    modified_text = input_text.lower().replace('r', 'w').replace('l', 'w')
    words = modified_text.split()
    modified_words = []
    for word in words:
        modified_words.append(word)
        if random.random() < 0.3:
            modified_words.append(random.choice(["uwu", "owo", "7w7", ":3", "^^", ">u<", "=^w^=", "x3", ">:3"]))
    modified_text = ' '.join(modified_words)
    return "~" + modified_text + " <3"

input_text = input("~Pwease entew youw message: ")
modified_message = modify_input(input_text)
print(modified_message)
