'''8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.'''



def send_messages(messages_list:list[str]):
    sent_messages:list[str] = [] 
    for i in range(len(messages_list) - 1, -1, -1):
        print(messages_list[i])
        sent_messages.append(messages_list.pop(i))

    
    return sent_messages


print(send_messages(["ciao", "salve", "arrivederci"]))
