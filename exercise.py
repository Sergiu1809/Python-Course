nume = input("Nume student: ")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

average = (nota1 + nota2 + nota3) / 3

status = "Passed"
if (average < 4.5):
    status = "Failed"

print(f"\nStudent: {nume}\nMedie: {average} \nStatus: {status}")
