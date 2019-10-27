"""
Lets do a basic math problem
"""

# TODO: perform all of the following mathematical operations and print the results in between
# TODO: set a constant tax rate of 20%
TAX = .20
print(TAX)
# TODO: ask a user what their profit was for the quarter
profit = input("What is your profit for this quarter so far?: ")
print(int(profit))
# TODO: deduct the tax rate from the profit and print the tax amount
answer = TAX * int(profit)
profit2 = int(profit) - answer
print(profit2)
# TODO: split that profit evenly amongst 7 share holders
answer2 = profit2 / 7.

print(answer2)
# TODO: print out what each shareholder will receive from the profit


# !! extra credit: print the remainder of the total profit divided by 6
