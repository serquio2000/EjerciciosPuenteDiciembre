def main():
    num1, num2 = int(input("introduce un numero")), int(input("introduce un numero"))
    while num1 > num2:
        num1, num2 = int(input("introduce un numero")), int(input("introduce un numero"))
    for num1 in range(num1, num2 + 1, 1):
        print(num1)


if __name__ == '__main__':
    main()
