# Create a program that:
# asks for student grades until user types "done"
# stores grades in a list
# prints:
# average
# highest grade
# lowest grade
# all grades above average

grades = []
average = 0

while True:
    x = input("What is your grade? ")

    if x.lower() == "done":
        break

    x = float(x)
    grades.append(x)

    sum1 = sum(grades)
    average = sum1 / len(grades)
    max1 = max(grades)
    min1 = min(grades)

    print(sum1)
    print(average)
    print(max1)
    print(min1)
    for grade in grades:
        if grade > average:
            print(grade)



