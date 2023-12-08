#!/usr/bin/python3
"""
0-prime_game
"""


def check_prime_nos(num):
    """
    Check for prime number
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    Maria = Ben = 0

    for i in range(x):
        prime_count = sum(1 for num in range(1, nums[i] + 1) if check_prime_nos(num))  # noqa: E501

        if prime_count % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    else:
        return None


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    Maria = Ben = 0

    for i in range(x):
        prime_count = sum(1 for num in range(1, nums[i] + 1) if check_prime_nos(num))  # noqa: E501

        if prime_count % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    else:
        return None
