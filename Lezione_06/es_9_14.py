'''9-14. Lottery: Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters. Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket. Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.
'''

import random
from typing import Any

class LotteryMachine():

    def __init__(self, item_list: list[Any] = [], winning_list: list[Any] = []):
        
        self.item_list = item_list
        self.winning_list = winning_list
    
    def setItemList(self, item_list) -> None:

        self.item_list = item_list


    def generateWinner(self) -> list[Any]:

        for i in range(4):
            random_index: int = random.randint(0, len(self.item_list) - 1)
            self.winning_list.append(self.item_list[random_index])
        
        return self.winning_list

    
    def showWinner(self) -> None:

        print(f"Any Ticket that matches this items: {self.winning_list} wins!")

    

if __name__ == "__main__":

    winning_ticket: LotteryMachine = LotteryMachine()

    winning_ticket.setItemList([1, "A", 9, 5, "G", "l", 7, "E", 0, "B"])

    winning_ticket.generateWinner()
    winning_ticket.showWinner()

