#########################################
# author: Jason Cariolano
# FIZZBUZZ
#########################################





print("********double input********")
r1 = int(input("Enter first number for range: "))
r2 = int(input("Enter second number for range: "))

if (r1>r2):
    r1, r2 = r2, r1 #always start at smallest number

for num in range(r1, r2+1):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 5!= 0 and num %3 != 0:
        print(num)
    
        
print("********single input********")        

sn = int(input("Enter a Number: "))
if sn % 5 == 0 and sn % 3 == 0:
        print("FizzBuzz")
elif sn % 3 == 0:
    print("Fizz")
elif sn % 5 == 0:
    print("Buzz")
elif sn % 5!= 0 and sn %3 != 0:
    sn = str(sn)
    print(sn + " is not Fizz or Buzz")
    
