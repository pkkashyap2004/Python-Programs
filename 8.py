def grade(marks):
    if marks >= 75 and marks <=100:
        print(marks, " in First Division." )
    elif marks >= 60 and marks <= 75:
        print(marks,"in Second Division.")
    elif marks >=50 and marks <= 60:
        print(marks , " in Third Division.")
    elif marks >= 40 and marks <= 50:
        print(marks ,"in Passing marks.")
    elif marks >= 0 and marks <= 40:
        print(marks,"Fail in Subject.")
    else:
        print(marks, "Not a valid marks.")
mark = int(input("Enter your marks even subject : "))
grade(mark)
