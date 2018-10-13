def namen():
    value = True

    students = {}

    while value:
        firstName = input("Volgende naam: ")
        if len(firstName.strip(" ")) == 0:

            for student in students:
                if(students[student]) == 1:
                    print("Er is " + str(students[student]) + " student met de naam " + student)
                else:
                    print("Er zijn " + str(students[student]) + " studenten met de naam " + student)

            value = False
        else:
            if firstName not in students:
                students[firstName] = 1
            else:
                students[firstName] += 1

namen()