'''3-7. Shrinking Guest List: You just found out that your new dinner table won't arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know 
you're sorry you can't invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they're still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.'''



guest_list:list[str] = ["Frodo Baggings", "Michael Scott", "Sheldon Cooper", "Tyrion Lannister"]
print("Hey everyone I found a bigger table!")
print("------------------------------------------------")
guest_list.insert(0, "Gandalf")
guest_list.insert(2, "Lionel Messi")
guest_list.append("Luke Skywalker")

print(f"Dear {guest_list[0]} you're invited to the party!")
print(f"Dear {guest_list[1]} you're invited to the party!")
print(f"Dear {guest_list[2]} you're invited to the party!")
print(f"Dear {guest_list[3]} you're invited to the party!")
print(f"Dear {guest_list[4]} you're invited to the party!")
print(f"Dear {guest_list[5]} you're invited to the party!")
print(f"Dear {guest_list[6]} you're invited to the party!")
print("------------------------------------------------")
print("Sorry everyone I can only invite 2 guests!")
print("------------------------------------------------")
uninvite:int = guest_list.pop(0)
print(f"I'm sorry {uninvite} you aren't invited anymore!")
uninvite:int = guest_list.pop(0)
print(f"I'm sorry {uninvite} you aren't invited anymore!")
uninvite:int = guest_list.pop(0)
print(f"I'm sorry {uninvite} you aren't invited anymore!")
uninvite:int = guest_list.pop(0)
print(f"I'm sorry {uninvite} you aren't invited anymore!")
uninvite:int = guest_list.pop(0)
print(f"I'm sorry {uninvite} you aren't invited anymore!")
print("------------------------------------------------")
print(f"Dear {guest_list[0]} you're invited to the party!")
print(f"Dear {guest_list[1]} you're invited to the party!")
print("------------------------------------------------")
del guest_list[:]
print(guest_list)









'''guest_list:list = ["Frodo Baggings", "Michael Scott", "Sheldon Cooper", "Tyrion Lannister"]
print("Hey everyone I found a bigger table!")
print("------------------------------------------------")
guest_list.insert(0, "Gandalf")
guest_list.insert(len (guest_list) // 2, "Lionel Messi")
guest_list.append("Luke Skywalker")

for guest in guest_list:
    print(f"Dear {guest} you're invited to the party!")
print("------------------------------------------------")
print("Sorry everyone I can only invite 2 guests!")
print("------------------------------------------------")
total_guests:int = len(guest_list)

for guest in range(total_guests):
    uninvite = guest_list.pop(0)
    print(f"I'm sorry {uninvite} you aren't invited anymore!")
    if guest == len(guest_list) + 2:
        break
print("------------------------------------------------")
for guest in guest_list:
    print(f"Dear {guest} you're still invited to the party!")

del guest_list[:]

print(guest_list)'''
