import csv
students=[
    {"RollNo":"101","Name":"Akshaya","Department":"CSE","Mark":98},{"RollNo":"102","Name":"Sowmiya","Department":"CSE","Mark":97},{"RollNo":"103","Name":"Vijay","Department":"CSE","Mark":96}

]
course=("Python",4)
print("Course Tuple:",course)
with open("students.txt","w") as file:
    for student in students:
        file.write(str(student)+"\n")
with open("students.csv","w",newline="") as file:
    fields=["RollNo","Name","Department","Mark"]
    writer=csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)
print("\n---Records from CSV---")
with open("students.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row["RollNo"],row["Name"],row["Department"],row["Mark"])
        