# Given a string S representing an amount of money in dollars, make change for that amount using the smallest number of coins and print the each used coin. Here are the available coins and their value:

# Dollar Coins: $1.00
# Quarters: $0.25
# Dimes: $0.10
# Nickels: $0.05
# Pennies: $0.01

# $4.58
# 4 2 0 1 3

# $8.90
# 8 3 1 1 0

# $0.49
# 0 1 2 0 4

# $6.00
# 6 0 0 0 0

# $0.01
# 0 0 0 0 1

testcases = ["$4.58", "$8.90", "$0.49", "$6.00", "$0.01"]
expected_results = ["4 2 0 1 3", "8 3 1 1 2", "0 1 2 0 4", "6 0 0 0 0", "0 0 0 0 1"]

import sys
import math

def get_change(s: str) -> str:
    # S is in the form $XXX.
    s = s[1:]
    amounts = s.split('.')
    dollars = int(amounts[0])
    change = int(amounts[-1])


    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    while (change > 0):
        if change >= 25:
            quarters += 1
            change -= 25
        elif change >= 10:
            dimes += 1
            change -= 10
        elif change >= 5:
            nickels += 1
            change -= 5
        else:
            pennies += 1
            change -= 1

    return f"{dollars} {quarters} {dimes} {nickels} {pennies}"
    

for i in range(len(testcases)):
    assert get_change(testcases[i]) == expected_results[i]