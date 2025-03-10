'''8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.'''


def send_messages(messages_list:list[str]):
    sent_messages:list[str] = [] 
    for i in range(len(messages_list) - 1, -1, -1):
        print(messages_list[i])
        sent_messages.append(messages_list.pop(i))

    
    return sent_messages

messages:list[str] = ["ciao", "salve", "arrivederci"]
copy_list:list[str] = messages[:]
print(send_messages(messages))
print(send_messages(copy_list))
