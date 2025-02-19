'''3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''



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
