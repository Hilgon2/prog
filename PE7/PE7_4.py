studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]


def gemiddelde_per_student(studentencijfers):
    cijfers = []
    for student in studentencijfers:
        cijfers.append(round(sum(student) / len(student), 2))
    return cijfers


def gemiddelde_van_alle_studenten(studentencijfers):
    cijfers = []
    for student in studentencijfers:
        for cijfer in student:
            cijfers.append(cijfer)
    gemiddelde = round(sum(cijfers) / len(cijfers), 2)
    return gemiddelde

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))