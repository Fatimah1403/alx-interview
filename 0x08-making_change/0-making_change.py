#!/usr/bin/python3
"""Making change
"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total

    Args:
        coins (list):  is a list of the values of the coins in your possessio
        total (int): the total amount to be made using the coins
    """
    # Initialize an array to store the minimum number
    # of coins needed for each total value
    count = [float('inf')] * (total + 1)

    # 0 coins needed to make a total of 0
    count[0] = 0

    # Iterate through each coin value
    for coin in coins:
        for i in range(coin, total + 1):
            count[i] = min(count[i], count[i - coin] + 1)

    # If count[total] is still float('inf'),total can't be made.
    if count[total] == float('inf'):
        return -1
    else:
        # Return the minimum number of coins needed for the given total
        return count[total]
