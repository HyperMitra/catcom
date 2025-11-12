#import nltk
#import random

#nltk.download('words')
#from nltk.corpus import words
#word_list = words.words()   
#print(random.choice(word_list)) 

#score=0


#q1 =input('capital of the seleucid empire:  ').lower()
#if q1 =='antioch':
    #print('correct')
    #score+=1
    #print('score')
#else:
    #print('wrong')




#q2 =input('capital of the roman empire:  ').lower()
#if q2 =='rome':
    #print('correct')
    #score+=1
    #print('score')
#else:
    #print('wrong')
    #print('score')



#def meme_function():
#   print('This is a meme function!')
#meme_function() 


#def meme_function():
#    return True 
#if meme_function():
 #   print('meme function exists!')
#else:
#    print('meme function does not exist!')
    
#first_name = "Bro"
#print(first_name)


#strings cant use ""
#age= 25
#quantity=3

#print(f"You are {age} years old and you have {quantity} items.")


#float integers but with decimal points

#price= 10.99
#print(f"the price is {price}")


#poop= False

#if poop:
#    print("You are not smelly")
#else:
#    print("You are smelly")


#is_student = False
#for_sale = True

#if for_sale:
#    print('This item is for sale')
#else:
 #   print('That item is not available')

#Typecasting = the process of converting a variable from one data type to another 
#str(), int(), float(), bool()

#name = "meowman"
#age =18
#strength=5.5
#is_human =False

#str()
#age = str(age)
#print(age)

##int()
#strength=int(strength)
#print(strength)

#age=float(age)
#print(age)


#age = str(age)

#age += "1"

#print(age)


#########input()########

## A function that prompts the user to enter data
# Returns the entered data as a string 

#name=input("what is your name?: ") 
#age=input("how old are you?: ")

#age= int(age)
#age= age + 1

#age=int(age)
#if age >= 18:
 #   print("you are an adult")
#else:
#    print("you are a minor")    

#print(f"hello {name}")
#print(f"you are {age} years old huh")


#exercise 1 rectangle area calculator

#length=input("what is the length of the rectangle?: ")
#width=input("what is the width of the rectangle?: ")

#length=int(length)
#width=int(width)

#area= length * width
#print(f"the area of the rectangle is {area}")


#answer=input("Iambic pentameter is made up of how many feet?: ")
#"(Answer with a number)"
#if answer == "5" :
#    print("Correct!")

#else:
#    print("Incorrect, the answer is 5.")

#loops##
#execute a block of code a fixed number of times.
# You can iterate overa range, string sequence, etc.

#for counter in range(1,7):
#    print(counter)

#for x in range(1,7):
#    print(x)

#print("Blast off!")

#import time
 
#for x in reversed(range(1,7)):
#   print(x)
 #   time.sleep(1) #pauses for 1 second between each number
#print("Blast off!")

#for x in range(1,7,11):
#    print(x)

#print("Blast off!")

#meow_call="124251-1231231-511612412-12312351251241"

#for x in meow_call:
#    print(x)


#for x in range(1,11):
#    if x ==10:
#        continue
#    else:
#        print(x)


#for x in range(1,11):
#    if x ==10:
#        break
#    else:
#        print(x)

#End the loop if i is larger than 3:

#for i in range(9):
#  if i > 3:
#    break
# print(i)


#i = 1
#while i < 6:
#    print(i)
#    if i == 3:
#      break 
#    i += 1

#import time
#while 1 == 1:
#    print("Meow")
#    print('Meow2')
 #   time.sleep(1)













#cat meow simulator



from datetime import datetime
import random
import time
 

current_time = datetime.now()



#cat time, simulation start

cat=input("Welcome to the cat meow simulator! Press Enter to continue...")  
time.sleep(1)

print(current_time.strftime("Current Date and Time: %Y-%m-%d %H:%M:%S"))
time.sleep(1)
#if current_time.hour <12:
#    print("The cat is doing good! It's morning time!")


#elif 12 <= current_time.hour <18:
#    print("the cat is sleeping")

#    exit()

#else: 
#    print("the cat is nowhere to be seen!")
    
#    exit()




#input#

cat = input("how is the cat feeling (hungry, sleepy, playful)?: ").lower()

if cat == "hungry":
    print ("cat is hungry")
    while True:
        import time
        time.sleep(1)
        action = input("feed the cat? (yes/no):").lower()  
        if action == "yes":
            print("you fed the cat")
            break
        elif action == "no":
            print("the cat is still hungry")
        else:
            print("Invalid input, please enter 'yes' or 'no'.")

elif cat == "sleepy":
    print ("cat is sleepy")
    while True:
        import time
        time.sleep(1)
        action = input("put the cat to sleep? (yes/no):").lower()
        if action == "yes":
            chance= random.randint(3,10)
            if chance > 5:
                print("the cat is resisting sleep")
            else:
                print("the cat is now sleeping")
                break
            
            

        elif action == "no":
            print('the cat is still awake')
        else:
            print("Invalid input, please enter 'yes' or 'no'.")

   
elif cat == "playful":
    print ("cat is playful")
    while True:
        import time 
        time.sleep(1)
        action = input ("play with the cat? (yes/no):").lower()
        if action == "yes":
            action = input ("choose where to play with the cat (background, meowpark, 222 avenue street)").lower()
            if action == "background":
                import time
                for i in range(5):
                    print(" 🐱 ")
                    time.sleep(1)
                print("the cat is bored in the background")
                time.sleep(1)

                print('You forgot about the cat and decided to do some activities on your own.')
                print (a := "Do some gardening")
                print (b := "Go for a walk")     
                print (c := "Go shopping")  

                action = input(f"Choose what you want to do next by replying with either a, b or c ({a} / {b} / {c}) :").lower()
                if action == "a":
                    print("You chose to do some gardening")
                    for i in range(5):
                        print("🌱🌿🌷🌻🌼")
                        time.sleep(1)
                    chance= random.randint(1,10)
                    if chance >7:
                        print("While gardening, the cat gains interest and starts playing with the plants.")
                        exit()
                    else:
                        print("You enjoyed gardening, but starts feeling guilty about neglecting the cat.")

                        exit()

                if action == "b":
                    text = "You choose to go for a walk"
                    for ch in text:
                        print(ch, end='', flush=True)
                        time.sleep(0.05)
                    print()



            elif action == "meowpark": 
                import time 
                for i in range(10):
                    print(" 🐱🛣️ ")
                    time.sleep(1)
                print('the cat enjoyed meowpark a lot!')
            
            elif action == '222 avenue street':
                import time 
                for i in range(10):
                    #for i in range prints the same words multiple times
                    print(" 🐱🛣️ ")
                    time.sleep(1)
                print ("the cat did not enjoy the avenue street too much")

            else:
                print("Invalid location choice.")
            break
        elif action == 'no':
            print("the cat is still playful")

        else:
            print('Invalid input, please enter "yes" or "no".')   



cat = input (("Are you taking the cat to the vet? (yes/no/maybe):").lower())
if cat == "yes":
    print("carries cat to car")
    time.sleep(1)
    print('drives to vet')
    time.sleep(1)
    print('arrives at vet')
    time.sleep(1)
    print('the vet checks the cat')
    time.sleep(1)
    print('the cat is healthy!')

elif cat == "no":
    print("meow")


elif cat == "maybe":
    print("you dont take the cat to the vet,~~~~")



else:
    print("Invalid input, please enter yes,no or maybe ")

    