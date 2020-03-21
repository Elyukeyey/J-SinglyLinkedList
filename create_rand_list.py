import linked_list
import random


# generate a random list up to 10000
def generate_list(amount):
    if amount > 10000:
        print(f'{amount} is more than the maximum allowed: 10000')
        return None

    i = 0
    list = linked_list.SinglyLinkedList()

    while i < amount:
        list.push(rand_value())
        i += 1

    return list


def rand_value():
    return random.randint(0, 80000)
