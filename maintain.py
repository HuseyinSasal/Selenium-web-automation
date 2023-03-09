print("HüseyinSasal")
title = "Car Loan"
print("title") 

#string => textual expression
title = "personal finance credit"
print("title")

#int , integer => 
vade = 14
ekVade = 5
vade2 ="42"

#float , decimal , double 
aylikOdeme = 200.50 

#bool , boolean => true or false 
yukselisteMİ = False

#mathematical operators (+)
print(2+2)
print(vade + 18)
print(vade + ekVade)
print(36 + 6)

#mathematical operators (-)
print(10-5)
print(vade - 12)
print(vade - ekVade)
print(29 - 6)

#mathematical operators (*)

print(2*2)
print(vade * 2)
print(vade * ekVade)
print(10*4)

#mathematical operators (/)
print(8/2)
print(vade / 2)
print(vade / ekVade)
print(40/4)


yenivade = vade / 2
fiyat = 130 
indirimliFiyat = fiyat - 20  

print(yenivade)
print(indirimliFiyat)


#Mod Operatörü %
print(8%2)
print(vade % 2)
print(vade % ekVade)
print(40 % 4)






#Logical Operators ==  
print(40 == 4 )
print(40 == 1 )
print(40 == 40 )

#Logical Operators >
print(40 > 4 )
print(40 > 1 )
print(40 > 40 )

#Logical Operators <

print(40 < 4 )
print(40 < 1 )
print(40 < 40 )

#Logical Operators <=

print(40 <= 4 )
print(40 <= 1 )
print(40 <= 40 )

#Logical Operators >=

print(40 >= 4 )
print(40 >= 1 )
print(40 >= 40 )

#ctrl + k c  

# Logical Operators >=
# print(40 >= 4 )
# print(40 >= 1 )
# print(40 >= 40 )

#Logical Operators !=
print(40 != 4 )
print(40 != 1 )
print(40 != 40 )

# or and => veya 

print (1 > 2 or 5 > 2 )
print (1 > 2 and  5 > 2 )
print (1 > 2 or  5 > 2 and 3 > 2  )

print (1 > 2 and  5 > 2 and 3 > 2  )

print (2 > 1 or  1 > 2 and 3 > 2  )





#if condition:  1   
#code block

paircar1 = 15
paircar2 = 15

if paircar1 < paircar2:
    print("paircar1 is greater than paircar2")
    print("inside of if block")
elif paircar1 == paircar2:
    print("paircar1 is equal to paircar2")
    print("inside of elif block")
else:
    print("paircar2 is greater than paircar1")
    print("inside of else block")

print("outside of if block")

if paircar1 <= paircar2:
    print("paircar1 is less than or equal to paircar2")
if paircar1 == paircar2:
    print("paircar1 is equal to paircar2")
else:
    print("paircar2 is greater than paircar1")

# result => paircar1 is less than or equal to paircar2  paircar1 is equal to paircar2

if paircar1 < paircar2:

    print("paircar1 is less than or equal to paircar2")
    if paircar1 == paircar2:
        print("paircar1 is equal to paircar2")
else:
    print("paircar2 is greater than paircar1")

# result => paircar2 is greater than paircar1


#-------------- 1st day 1. Homework
#Example 1

#Use python which calculates the average of 3 midterm (60%) and final (40%) grades received from the user.

visa1 = float(input('visa1:'))
visa2 = float(input('visa2: '))
visa3 = float(input('visa3: '))
final = float(input('final : '))

average = ((visa1+visa2+visa3)/3)*0.6 + (final * 0.4)

result = (average>=50) and (final>=50)
result = (average >=50) or (final>=70)



if (average>=50):
     
     if (final>=50):
          print(f'student average: {average} and passa status: successful')
     else:
          print(f'student average: {average} and pass status: failed. You must get at least 50 from the final.')
else:
     print(f'student average:: {average} and pass status: failed')



if (ortalama >=50):
    print(f'student average:: {average} and passa status: successful')
else:
    if (final>=70):
        print(f'student average:: {average} and pass status: successful. You passed the final because you got at least 70.')

    print(f'student average: {average} and pass status: failed')




#Example 2
