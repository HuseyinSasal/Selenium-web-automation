#Thursday March 9,2023

#-------------- 1st day 1. Homework
#Example 1

#Use python which calculates the average of 10 midterm (60%) and final (40%) grades received from the user.

visa1 = float(input("visa1:"))
visa2 = float(input("visa2: "))
visa3 = float(input("visa3: "))
visa4 = float(input("visa4:"))
visa5 = float(input("visa5: "))
visa6 = float(input("visa6: "))
visa7 = float(input("visa7:"))
visa8 = float(input("visa8: "))
visa9 = float(input("visa9: "))
visa10 = float(input("visa10:"))


final = float(input("final : "))

average = ((visa1+visa2+visa3+ visa4+visa5+visa6+visa7+visa8+visa9+visa10)/3)*0.6 + (final * 0.4)

result = (average>=50) and (final>=50)
result = (average >=50) or (final>=70)



if (average>=50):
     
     if (final>=50):
          print("student average: {average} and passa status: successful")
     else:
          print("student average: {average} and pass status: failed. You must get at least 50 from the final.")
else:
     print("student average:: {average} and pass status: failed")



if (average >=50):
    print("student average:: {average} and passa status: successful")
else:
    if (final>=70):
        print("student average:: {average} and pass status: successful. You passed the final because you got at least 70.")

    print("student average: {average} and pass status: failed")


#-------------- 1st day 1. Homework
#Example 2

#Make a python application that compares 4 entered numbers in size.

W = int(input("W: "))
X = int(input("X: "))
Y = int(input("Y: "))

if (W > X) and (W > Y):
    print("W is the largest number.")
elif (X > W ) and (X  > Y):
    print("X is the largest number.")
elif (Y > W) and (Y > X):
    print("Y is the largest number.")
