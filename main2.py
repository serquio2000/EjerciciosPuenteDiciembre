def main():
    n = int(input("introduce cuantas notas quieres introducir:"))
    marks, x, aprobado, suspenso = 0, 0, 0, 0
    countPass, countFail, passed, failed = 0, 0, float(0), float(0)
    avgPass = list()
    avgFail = list()
    while n < 1:
        n = int(input("introduce cuantas notas quieres introducir:"))
    while x < n:
        marks = float(input("introduce la nota del alumno:"))
        while marks < 0 or marks > 10:
            marks = float(input("introduce la nota del alumno:"))
        if marks > 4:
            avgPass.append(marks)
            aprobado += 1
        else:
            avgFail.append(marks)
            suspenso += 1
        x += 1
    print("el resultado de las notas suspendidas: ")
    while countFail < suspenso:
        failed = avgFail[countFail] + failed
        print(avgFail[countFail])
        countFail += 1
    print("el resultado de las notas aprobadas: ")
    while countPass < aprobado:
        passed = avgPass[countPass] + passed
        print(avgPass[countPass])
        countPass += 1
    print("la mediana de los aprobados es:")
    print(passed / countPass)
    print("la mediana de los suspensos es:")
    print(failed / countFail)
if __name__ == "__main__":
    main()
