'''8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.'''


def show_messages(messages_list:list[str]):
    for message in messages_list:
        print(message)

show_messages(["ciao", "salve", "arrivederci"])