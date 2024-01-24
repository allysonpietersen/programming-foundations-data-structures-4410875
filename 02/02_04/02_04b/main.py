''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

#identify which item in the list you want to modify
#change the value at the index to be a new number
student_pet_count_list[2] = 3 
#adding a value to the current index
student_pet_count_list[3] = student_pet_count_list[3] + 1
student_pet_count_list[-1] = student_pet_count_list[-1] + 2

#adding new students with pets to the list
student_pet_count_list.append()

NUM_OF_STUDENTS = len(student_pet_count_list)
print(NUM_OF_STUDENTS)
SUM = 0
for INDIVIDUAL_PET_COUNT in student_pet_count_list:
    SUM = SUM + INDIVIDUAL_PET_COUNT
print(SUM)

AVERAGE = SUM / NUM_OF_STUDENTS
print(AVERAGE)
