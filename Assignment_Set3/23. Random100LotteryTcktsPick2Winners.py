# 23. Generate 100 random lottery tickets and pick two lucky tickets from it as a
# winner.

import random

tickets = random.sample(range(10000,99999),100)
print("Lottery Tickets: ")
print(tickets)

winners = random.sample(tickets,2)
print("Lucky Winners: ")
print(winners)

