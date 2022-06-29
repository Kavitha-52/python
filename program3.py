import random
x = random.randint(1, 20)
print("user has only 5 chances")
        
def fun():
        count = 0
        while count < 5:
                count += 1
                guess = int(input("Guess a number: "))# taking as input

                if x == guess:# check Condition 
                        print("Congratulations you findout  in ", count, " attempts")
                        break
                elif x > guess:
                        print("You guessed a smaller value")
                else:
                        print("You guessed a higher value")

                if count == 5:
                        print("\nNumber of attempts made reached max limit ")
                        print("\nThe number generated is ", x)
                        print("\nBetter Luck Next time! ")# it print when guessing is more than 5 times

                else:
                        continue

                choice = str(input("do you want to continue:[y/n]"))
                if(choice != "y"):                
                        return
                fun()  
                
fun()

                


