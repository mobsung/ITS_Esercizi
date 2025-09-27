'''
Per gli apprendisti, misura l’esborso più efficiente. Realizza `min_coins(amount, coins)` restituendo il conteggio minimo, o `1_000_000_000` quando non componibile. Mantieni la firma e promuovi i test.
'''

def min_coins(amount, coins):

    dp = [1_000_000_000] * (amount + 1)
    dp[0] = 0 

    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != 1_000_000_000 else 1_000_000_000


# print(min_coins(11,[1,2,5]))
# print(min_coins(0,[1,2,5]))
# print(min_coins(3,[2]))
# print(min_coins(6,[1,3,4]))
print(min_coins(7,[1,2,5]))
# print(min_coins(2,[2]))

