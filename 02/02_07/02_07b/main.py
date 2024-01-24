# Linear Search

my_list = [8, 5, 0, 3, 9, 7]
ITEM = 7

def search(item, listy):
  for element in listy:
    if element == item:
      return True
    return False
  
print(search(ITEM, my_list))

#search for 1st occurance of index in list and use result to return item
ITEM_INDEX = my_list.index(ITEM)

