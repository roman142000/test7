grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
student = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# a = (sum(grades[0]) / len(grades[0]))
# b = (sum(grades[1]) / len(grades[1]))
# c = (sum(grades[2]) / len(grades[2]))
# d = (sum(grades[3]) / len(grades[3]))
# e = (sum(grades[4]) / len(grades[4]))

student = sorted(student)
print({student[0]: sum(grades[0]) / len(grades[0]),
       student[1]: sum(grades[1]) / len(grades[1]),
       student[2]: sum(grades[2]) / len(grades[2]),
       student[3]: sum(grades[3]) / len(grades[3]),
       student[4]: sum(grades[4]) / len(grades[4])})



