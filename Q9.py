string=input("Enter a value which contains 'Python':")
int_input=int(input("Enter a value which contains the number 10:"))
float_input=float(input("Enter a value which contains float 100.0:"))
statments=[string=="Python",int_input==10,float_input==100.0]
if all(statments):
    print(string)
    print(int_input)
    print(float_input)
else:
    print("one of the inputs doesn't match the target")
