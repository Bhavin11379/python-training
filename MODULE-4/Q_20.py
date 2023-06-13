#20) Write python program that user to enter only odd numbers, else will raise an exception.

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
