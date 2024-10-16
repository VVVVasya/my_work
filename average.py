grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
grade_1 = sum(grades[0][:]) / len(grades[0][:])
grade_2 = sum(grades[1][:]) / len(grades[1][:])
grade_3 = sum(grades[2][:]) / len(grades[2][:])
grade_4 = sum(grades[3][:]) / len(grades[3][:])
grade_5 = sum(grades[4][:]) / len(grades[4][:])
grades_list = []
grades_list.append(grade_1)
grades_list.append(grade_2)
grades_list.append(grade_3)
grades_list.append(grade_4)
grades_list.append(grade_5)
pairs = dict(zip(students, grades_list))
print(pairs)
