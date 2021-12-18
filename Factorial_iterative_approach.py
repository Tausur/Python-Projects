def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

user = int(input("Enter the number: "))
print(f"The factorial of {user} is {factorial(user)}")