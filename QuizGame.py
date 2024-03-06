print(" Welcome to my Computer Quiz Game !") 
playing = input("Do you want to play ? ")

if playing.lower() != "yes" :
    quit()

print("OKAY ! Lets Play :)" )
score = 0

answer = input("1. What does CPU stands for ? ")
if answer.lower() == "central processing unit" :
    print(" Correct !")
    score += 1  #Score = Score + 1 --> To increment score by one.
    print("Score : " + str(score))
    
else :
    print(" Incorrect!")
    
    
answer = input("2. What does RAM stands for ? ")
if answer.lower() == "random access memory" :
    print(" Correct !")
    score += 1
    print("Score : " + str(score))
    
else :
    print(" Incorrect!")
    

answer = input("3. What does ROM stands for ? ")
if answer.lower() == "read only memory" :
    print(" Correct !")
    score += 1
    print("Score : " + str(score))

else :
    print(" Incorrect!")


answer = input("4. What does IC stands for ? ")
if answer.lower() == "integrated circuit" :
    print(" Correct !")
    score += 1
    print("Score : " + str(score))

else :
    print(" Incorrect!")

answer = input("5. What does GPU stands for ? ")
if answer.lower() == "graphics processing unit" :
    print(" Correct !")
    score += 1
    print("Score : " + str(score))

else :
    print(" Incorrect!")

answer = input("6. What does PSU stands for ? ")
if answer.lower() == "power supply unit" :
    print(" Correct !")
    score += 1
    print("Score : " + str(score))

else :
    print(" Incorrect!")

print("You got " + str(score) + " Questions Correct !")
print("You got " + str((score / 6) * 100) + " %.")
    

