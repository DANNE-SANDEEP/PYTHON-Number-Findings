import random
num=int(input("Enter starting range: "))
num1=int(input("Enter ending range: "))
number=random.randint(num,num1)
def prime_number(number):
    if number > 1:
    # Iterate from 2 to n / 2
        for i in range(2, int(number/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
            if (number % i) == 0:
                print(number, "is not a prime number")
            break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
if number>0:
    print("{} is a positive number".format(number))
if number<0:
    print("{} is a negitve number".format(number))
if number%2==0:
    print("{} is a even number".format(number))
if number%2!=0:
    print("{} is a odd number".format(number))
prime_number(number)