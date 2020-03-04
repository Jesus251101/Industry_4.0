name=input("What is your name?")
print("Hi!!", name)   
print("What is your age?")
age = float(input())
print("What is you height?")
height =float(input())
if age>=18:
    print("You are ",age, "years")    
    print("You can now vote" )
    answer=input("You can to have driving permit. Do you have it?(Y/N)")
    if answer == 'y':
        print("You can drive")
    if answer == 'n':
        print("You can get a driving lincese")
else:
    print("You are ",age, "years")
    print("You don´t can now vote")
    print("You cann´t to have driving permit.")
    
if height>=170 :
    print("You are tall")
elif height>=160:
    print("You are medium" )
else:
    print("You are short")


    