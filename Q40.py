def convert(weight,height):
    BMI=weight/height**2
    return BMI


x=True
while x:
    method= int(input("(1).KG/Meter\n"
                       "(2).pound/ inch\n"
                       "Enter The Method Number:"))


    if method==1 or method==2:

        x=False
        if method == 1:
            weight = float(input("please Enter the weight(KG):"))
            height = float(input("please Enter the height(CM):"))
            height=height*0.01
            IBM=convert(weight,height)
        else:
            weight = float(input("please Enter the weight(LBS):"))
            height = float(input("please Enter the height(inches):"))
            weight=weight*0.4535
            height=height*0.0254
            convert(weight, height)
            IBM = convert(weight, height)


    else:
        print("///////////////////////////////")
        print("**please Enter The Method value*")
        print("///////////////////////////////")
print(round(IBM, 2))




