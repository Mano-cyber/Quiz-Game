print("Welcome To My Quiz")

playing = input("Do You Want To Play? ")

if playing.lower() !="yes":
    quit()

print("Let's Play!")
score = 0

#Q1
answer = input("What CPU stand for? ")

if answer.lower() == "central processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect")

#Q2
answer = input("What does HDD stand for? ")

if answer.lower() == "hard disk drive":
    print('Correct')
    score += 1
else:
    print("Incorrect")

#Q3
answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print('Correct')
    score += 1
else:
    print("Incorrect")

#Q4
answer = input("What dies SQL stand for? " )

if answer.lower() == "structured query language":
    print('Correct')
    score += 1
else:
    print("Incorrect")

#Q5
answer = input("What is the language used to program games ? " )

if answer.lower() == "python":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/5) *100) + "%")