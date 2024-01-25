from collections import deque

def check_matching_parenthese(s):
  stack = deque()
  for char in s:
    if char == "(":
      stack.append(char)
    elif char == ")":
      if not stack:
        return False
      stack.pop()
  return len(stack) == 0

print(check_matching_parenthese("()"))
print(check_matching_parenthese("(hi there)"))
print(check_matching_parenthese("(hell)o"))
print(check_matching_parenthese("((linkedin)) learning"))

print(check_matching_parenthese("(hi(there"))
print(check_matching_parenthese("()ok)"))
print(check_matching_parenthese("((increment)"))
print(check_matching_parenthese(")linkedin()"))