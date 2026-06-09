A = int(input("Input the first number: "))
B = int(input("Input the second number: "))

if A > B:
    A1 = A - B
    print(f"{A} - {B} = {A1}")
    
elif B > A:
    A2 = B - A
    print(f"{B} - {A} = {A2}")

else:
    print(f"{A} and {B} are the same.")