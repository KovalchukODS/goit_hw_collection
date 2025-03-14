import random

def get_numbers_ticket(min, max, quantity : int) -> list:
    if min < 1 or max > 1000 or (max - min + 1) < quantity: return []
    lottery_list = random.sample(range(min, max + 1), quantity) 
    return lottery_list

print(get_numbers_ticket(1, 4, 4))

def get_numbers_ticket2(min, max, quantity : int) -> set :
    lottery_set = set()
    if min < 1 or max > 1000 or (max - min + 1) < quantity: return lottery_set
    while len(lottery_set) != quantity:
        lottery_set.add(random.randint(min, max))
    return lottery_set

print(get_numbers_ticket2(1, 4, 4))
