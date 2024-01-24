my_list = [1, 7, 3]
print(sorted(my_list))

#sort in descending order
print(sorted(my_list, reverse=True))

#deal with tuples
student_grades = [('Sarah', 89), ('Rebecca', 82), ('Matt', 91)]
print(sorted(student_grades)) #will sort based on 1st item in tuple
print(sorted(student_grades, key=lambda x:x[1], reverse=True)) #sort based on desc order of grade
