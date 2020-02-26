name=input("What is your name?")
print("Hi!!", name)   
print("What is your age?")
age = float(input())
print("What is you height?")
height =float(input())
if age>=18:
    print("You are ",age, "years")    
    print("You can now vote" )
else:
    print("You are ",age, "years")
    print("You don´t can now vote")
if height>=160:
    print("You are medium")
elif height>=170:
    print("You are tall" )
else:
    print("You are short")