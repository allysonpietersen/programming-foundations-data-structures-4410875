set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

#combine the two sets using union operation to create a new set
#sets do not contain duplicates, only one value for each will be added
union_set = set_A.union(set_B)
print(union_set)

#see what values are in both sets
intersection_set = set_A.intersection(set_B)
print(intersection_set)

#difference allows us to remove contents of one set or another
#subtract contents of set B from set A
difference_set = set_A.difference(set_B) 
print(difference_set)

difference_setBA = set_B.difference(set_A)
print(difference_setBA)

#elements unique to both sets use symmetric function
#will contain all the items the sets do not share
symmetric_difference_set = set_A.symmetric_difference(set_B)
print(symmetric_difference_set)