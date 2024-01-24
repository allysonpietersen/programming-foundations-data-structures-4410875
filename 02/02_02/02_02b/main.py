''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

#creating and initializing a list with values
student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

#accessing items at specifc index
ITEM_AT_INDEX_THREE = student_pet_count_list[3]
# print(student_pet_count_list[100])
ITEM_THREE_FROM_BACK = student_pet_count_list[-3]

#tell us how many numbers are in the data structure
NUM_OF_STUDENTS = len(student_pet_count_list)
print(NUM_OF_STUDENTS)

#creating for loop to add each item to the entry of the sum
SUM = 0
for INDIVIDUAL_PET_COUNT in student_pet_count_list:
  SUM = SUM + INDIVIDUAL_PET_COUNT
print(SUM)

# average = sum / number of items
AVERAGE = SUM / NUM_OF_STUDENTS
print(AVERAGE)