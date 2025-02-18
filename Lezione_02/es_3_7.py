'''3-7. Shrinking Guest List: You just found out that your new dinner table won't arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know 
you're sorry you can't invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they're still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.'''



guest_list:list = ["Frodo Baggings", "Michael Scott", "Sheldon Cooper", "Tyrion Lannister"]
print("Hey everyone I found a bigger table!")

guest_list.insert(0, "Gandalf")
guest_list.insert(2, "Lionel Messi")
guest_list.insert(len(guest_list), "Luke Skywalker")

#for invites in guest_list:
    #print(f"Dear {invites} you're invited to the party!")

print("Sorry everyone I can only invite 2 guests!")
#total_guests:int = len(guest_list)
for index in range(len(guest_list)):
    uninvite = guest_list.pop(index)
    print(f"I'm sorry {uninvite} you aren't invited anymore!")
    if index == len(guest_list):
        print(guest_list)
        break 