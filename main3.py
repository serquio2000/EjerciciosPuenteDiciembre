def main():
    username = list()
    department = list()
    classroom = list()
    user_name, dep, clr = "", "", 0
    x, y = 0, 0
    users = int(input("introdcue cuantos usuarios deseas añadir:"))
    while x < users:
        user_name = input("introduce tu nombre:")
        dep = input("introduce tu departamento:")
        clr = int(input("introduce el numero de aula:"))
        while clr > 15 or clr < 1:
            clr = int(input("introduce el numero de aula:"))
        username.append(user_name)
        department.append(dep)
        classroom.append(clr)
        x += 1
    print("\tusuario " + "\tdepartamento " + "\tclase ")
    while y < len(username):
        print("\t", username[y],"\t",department[y], "\t", classroom[y])
        y += 1


if __name__ == "__main__":
    main()
