import django_setup
from schedule.models import Subject, Teacher, Class, Student, Schedule, Grade


while True:
    print("1. Add Subject")
    print("2. Add Teacher")
    print("3. Add Class")
    print("4. Add Student")
    print("5. Add Schedule")
    print("6. Add Grade")
    print("7. Exit")
    
    choice = input("Your choice: ")

    if choice == '1':
        subject_name = input("Enter subject name: ")
        Subject.objects.get_or_create(name=subject_name)

    elif choice == '2':
        teacher_name = input("Enter teacher name: ")
        subject_name = input("Enter subject for the teacher: ")
        subject = Subject.objects.get(name=subject_name)
        Teacher.objects.get_or_create(name=teacher_name, subject=subject)

    elif choice == '3':
        class_number = int(input("Enter class number: "))
        class_letter = input("Enter class letter: ")
        Class.objects.get_or_create(number=class_number, letter=class_letter)

    elif choice == '4':
        student_name = input("Enter student name: ")
        class_number = int(input("Enter class number: "))
        class_letter = input("Enter class letter: ")
        student_class = Class.objects.get(number=class_number, letter=class_letter)
        Student.objects.get_or_create(name=student_name, students_class=student_class)

    elif choice == '5':
        day = input("Enter day (Monday, Tuesday, Wednesday, Thursday, Friday): ")
        lesson_number = int(input("Enter lesson number (1-7): "))
        subject_name = input("Enter subject name: ")
        class_number = int(input("Enter class number: "))
        class_letter = input("Enter class letter: ")
        teacher_name = input("Enter teacher name: ")

        subject = Subject.objects.get(name=subject_name)
        lesson_class = Class.objects.get(number=class_number, letter=class_letter)
        teacher = Teacher.objects.get(name=teacher_name)
        Schedule.objects.get_or_create(day=day, lesson_number=lesson_number, subject=subject, lesson_class=lesson_class, teacher=teacher)
    
    elif choice == '6':
        student_name = input("Enter student name: ")
        subject_name = input("Enter subject name: ")
        grade_value = int(input("Enter grade value (1-12): "))

        student = Student.objects.get(name=student_name)
        subject = Subject.objects.get(name=subject_name)
        Grade.objects.get_or_create(student=student, subject=subject, grade=grade_value)
    
    elif choice == '7':
        break
