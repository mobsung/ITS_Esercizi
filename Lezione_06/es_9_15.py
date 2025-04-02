'''9-15. Lottery Analysis: Extend the LotteryMachine class you created in Exercise 9-14.

1. Add a method called simulate_until_win(self, my_ticket) that:

Accepts a ticket (a list of 4 items).
Repeatedly draws random tickets using the draw_ticket() method.
Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
Returns the number of attempts and the winning ticket.
2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

4. Print a message showing:

Your ticket
The winning ticket
How many attempts it took to win
'''


import random
from typing import Any

class LotteryMachine():

    def __init__(self, item_list:list[Any] = [], winning_list: list[Any]= [], my_ticket: list[Any] = []):
        
        self.item_list : list[Any] = item_list
        self.winning_list: list[Any] = winning_list
        self.my_ticket: list[Any] = my_ticket
    
    def setItemList(self, item_list) -> None:

        self.item_list = item_list


    def generateWinner(self) -> list[Any]:

        for i in range(4):
            random_index: int = random.randint(0, len(self.item_list) - 1)
            self.winning_list.append(self.item_list[random_index])
        
        return self.winning_list

    
    def showWinner(self) -> None:

        print(f"Any Ticket that matches this items: {self.winning_list} wins!")

    
    def pickTicket(self) -> list[Any]:

        while len(self.my_ticket) < 4:

            item :str = input(f"Choose 4 character in from this list: {self.item_list}!\n==>")

            if item.upper() in self.item_list:
                self.my_ticket.append((item).upper())
            else:
                print(f"The item >{item}< is not in the list!")

        return self.my_ticket


    def simulate_until_win(self):

        draws:int = 0

        while self.winning_list != self.my_ticket:

            self.winning_list = self.generateWinner()
            
            draws += 1
            if self.winning_list != self.my_ticket:
                print(f'Winning list: {self.winning_list}')
                self.winning_list = []
            print(f'My ticket: {self.my_ticket}')
        
        print(f'You won in a total of {draws} draws')


if __name__ == "__main__":

    my_ticket: LotteryMachine = LotteryMachine()
    draw_ticket: LotteryMachine = LotteryMachine()
    item_list: LotteryMachine = LotteryMachine()


    my_ticket.setItemList(["1", "A", "9", "5", "G", "L", "7", "E", "0", "B"])

    my_ticket.pickTicket()

    my_ticket.simulate_until_win()

