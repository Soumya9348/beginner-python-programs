def multiplication_table(n):
    for i in range(1,11):
        print(n,' x ', i, ' = ',n*i)
    return ''
n = int(input("Enter the number: "))
print(multiplication_table(n))
