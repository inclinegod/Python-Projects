import random

name = ("Alex")
question = ("")
answer = ""
random_number = random.randint(1, 9)

if len(name) == 0:
      print(question)
      print("Outlook not so good!")

elif len(question) == 0:
      random_number = 0
      print("The magic-8-ball cannot provide a fortune otherwise, the fabric of reality is at risk!")
elif random_number == 1:
    answer =("Yes = definitely ")
elif random_number ==2:
    answer = ("It is decidedly so ")
elif random_number ==3:
    answer = ("Without a doubt ")
elif random_number ==4:
    answer = ("Reply hazy, try again! ")
elif random_number ==5:
    answer = ("Ask again later ")
elif random_number ==6:
    answer = ("Better not tell you now ")
elif random_number ==7:
    answer = ("My sources say no ")
elif random_number ==8:
    answer = ("Outlook not so good ")
elif random_number ==9:
    answer = ("Very Doubtful ")
else:
    print("error")


if len(name) >= 1 and len(question) >=1:
  print(name, "Asks", question,)
  print("Magic 8 balls answer: ", answer)
else:
    if len(name) == 0:
      print("\n no name inputted")
    elif len(question) == 0:
      print("\n no question inputted")
