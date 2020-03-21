import node
import linked_list
import random

def generate(amount):
  i = 0
  list = linked_list.SinglyLinkedList()

  while i < amount:
    list.push(rand_value())
    i += 1

  return list  


def rand_value():
  return random.randint(0, 100000000000)