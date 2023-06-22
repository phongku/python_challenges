import csv

user_file = input()

students = []
with open(user_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        line = row[0].split('\t')
        students.append({'last_name': line[0], "first_name": line[1], "mt1": line[2], "mt2": line[3], "fin": line[4]})

for i in students:
    student_avg = (int(i['mt1']) + int(i['mt2']) + int(i['fin'])) / 3
    if student_avg >= 90:
        student_grade = "A"
    elif 80 <= student_avg < 90:
        student_grade = "B"
    elif 70 <= student_avg < 80:
        student_grade = "C"
    elif 60 <= student_avg < 70:
        student_grade = "D"
    else:
        student_grade = "F"
    i["letter_grade"] = student_grade
    
midterm1 = 0
for i in range(len(students)):
    midterm1 += int(students[i]['mt1'])

midterm1 /= len(students)

midterm2 = 0
for i in range(len(students)):
    midterm2 += int(students[i]['mt2'])

midterm2 /= len(students)

final = 0
for i in range(len(students)):
    final += int(students[i]['fin'])

final /= len(students)

file_path = 'report.txt'
with open(file_path, 'w') as file:
    for i in range(len(students)):
        together = '\t'.join(students[i].values())
        file.write(together + '\n')
    file.write('\n' + f'Averages: midterm1 {midterm1:.2f}, midterm2 {midterm2:.2f}, final {final:.2f}' + '\n')
