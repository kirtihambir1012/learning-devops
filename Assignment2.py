# #Q1
# # Grade Checker
# # Take a score as input and print the grade based on the following:
# # 90+ : "A"
# # 80-89 : "B"
# # 70-79 : "C"
# # 60-69 : "D"
# # Below 60 : "F"
# # here we used a basic if else statement to carry out marks and all.

###   Approach1   ###

# score = int(input("Enter your score: "))

# if score >= 90:
#     print("A")
# elif 80<=score<=89:
#     print("B")
# elif 70<=score<=79:
#     print("C")
# elif 60<=score<=69:
#     print("D")
# else:
#     print("F")

###   Approach 2    ####

# score = int(input("Enter your score: "))

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")


# # 2 Student Grades
# # Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
# # Add a new student and grade.
# # Update an existing student’s grade.
# # Print all student grades.

# students = {
#     'kirti': 75,
#     'rushi': 82,
#     'amol': 95,
#     'vinita': 89
# }


# # To add new student
# def addnew():
#     name = input("Enter name: ")
#     grade = int(input("Enter grade: "))
#     students[name]=grade

# def updategrade():
#     update_name = input("Enter student's name: ")
#     if update_name in students:
#         update_grade = input("Enter grade to upgrade: ")
#         students[update_name] = update_grade

# def printlist():
#     print(students)

# def start():
#     print("========================================")
#     print("1: Add a new student and grade")
#     print("2: Update an existing student’s grade")
#     print("3: Print all student grades")
#     print("4: EXIT")
#     choice=int(input("Enter choice: "))

#     if choice==1:
#         addnew()
#         start()
#     elif choice==2:
#         updategrade()
#         start()
#     elif choice==3:
#         printlist()
#         start()
#     elif choice==4:
#         print("You pressed exit")    
#     else:
#         print("Invalid option")
#         start()

# start()    
# 


# # 3.Write to a File
# # Write a program to create a text file and write some content to it.
# # Using file functions like write and open.
# # Create a file and write content to it

# file = open("test1.txt", "w")

# file.write("Hello, World!\n")
# file.write("This is a text file.\n")
# file.write("Learning file handling in Python.")

# file.close()

# 4. Read from a File
# We used open to open file in read mode and file.read to read and print to display.

# to Open
file = open("test1.txt", "r")
# to Read
content = file.read()
# to Display
print(content)

file.close()
    