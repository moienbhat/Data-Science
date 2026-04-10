try:
    x = int(input("Enter the number : "))
    ans = 10 / x

except ZeroDivisionError:
    print("Divide by zero error occured")
except ValueError:
    print("Invalid input")

else:
    print(f"Answer is {ans}")

finally:
    print("This is end of the program")

