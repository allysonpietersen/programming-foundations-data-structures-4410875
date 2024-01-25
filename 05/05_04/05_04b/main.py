#create a function that prints out 1st n binary numbers
from collections import deque

#Pattern of binary num:
#1
#10
#11
#101
#110
#111
#1000

def print_binary_num(n):
  if n <= 0:
    return
  
  queue = deque()
  queue.append(1)

  for i in range(n):
    binary = queue.popleft()
    print(binary)
    queue.append(binary * 10)
    queue.append(binary * 10 + 1)

print_binary_num(6)
print()
print_binary_num(-9)
print()
print_binary_num(0)
print()
print_binary_num(2)
print()