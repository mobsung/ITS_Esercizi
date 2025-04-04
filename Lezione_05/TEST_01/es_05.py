'''
Nel gioco del Blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. Ogni carta ha un valore compreso tra 2 e 11 inclusi.

    Il valore numerico delle carte (da 2 a 10) è equivalente al loro valore nominale.
    Le figure (Jack, Regina, Re) non sono incluse in questo esercizio e vengono ignorate.
    L'Asso (valore 11) può valere 1 o 11, a seconda di quale sia più favorevole al giocatore:
        Se la somma della mano supera 21, e c'è almeno un asso valutato 11, quell'asso deve essere considerato 1 per evitare il "bust" (superare 21).

Scrivi una funzione che prende in input una lista di interi rappresentanti i valori delle carte e restituisce il valore totale della mano secondo le regole del Blackjack.
'''


def blackjack_hand_total(cards: list[int]) -> int:

    hand:int = 0
    temp_cards:list[int] = []

    for char in cards:
        if char != 11 and char != 1:
            hand += char
        elif char == 11 or char == 1:   
            temp_cards.append(char)
    
    for char in temp_cards:
        if hand + char <= 21:
            hand += char
        else:
            hand += 1
        
    return hand




print(blackjack_hand_total([11, 10, 5]))