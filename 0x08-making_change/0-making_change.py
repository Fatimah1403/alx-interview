#!/usr/bin/python3
"""Making change
"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total

    Args:
        coins (list):  is a list of the values of the coins in your possessio
        total (int): the total amount to be made using the coins
    """
    i = 0
    counter = 0
    num_coins = len(coins)
    sum = 0
    coins.sort(reverse=True)
    
    
    if total <= 0:
        return 0
    
    while sum < total and i < num_coins:
        while coins[i] < total - sum:
            sum += coins[i]
            counter += 1
            if sum == total:
                return counter
        i += 1
    return -1
    
   