











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

    
