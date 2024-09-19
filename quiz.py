
#Creating a quiz game for an user and displaying how much do they win after playing the game



questions =["What is the highest peak in the world: ","What is 5+5: ","what is the biggest continent in the world: ","In which continent Nepal is located: "]

answers = ["Mount Everest", 10, "Asia", "Asia" ]

score = 0

print("There will be 4 questions in total \n And every question has 1 mark \n The highest you can score is 4 \n Let's start the game \n \n ")


for i in range(len(questions)):
    print(questions[i])
    user= input("enter your answer ")
 

    if str(user).lower()==str(answers[i]).lower():
        print("correct")
        score+=1
    else:
        print("wrong, the correct answer is ",answers[i])
 

print("your total score is ", score, " out of ", len(questions))
 

 

 