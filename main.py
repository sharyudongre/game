
#this is the link to the code on repl.it
https://repl.it/@sharyuDongre/game#main.py

# written code:

print("Welcome to the game!")
name=input("ENTER YOUR NAME : ")
print ("Hello ",name,"!")
age=int(input("ENTER YOUR AGE : "))
print("You are ", age,"years old.")
bonus=0
if age>18:
  print("Congratulations!,you are eligible to play the game")
  ask=input("Do you want to play the game?...enter \"yes\" or \"no\"").lower()
  if ask=="yes":
    bonus=50
    print("Great,You have earned 50 bonus points.Lets start the game!")
    direction=input("Pick a direction you want to go (left/right)?").lower()
    if direction =="left":
      ans=input("Great!,You go left,follow the path and reach a lake.....Now do you swim across or go around(swim across/go around)?").lower()

      if ans=="swim across":
        bonus=bonus-10
        print("point=",bonus)
        print("You have reached the other end.But you have lost 10 points.Now you find a litte hut.")
        hut=input("Will you go inside the hut or move ahead in the path?(move ahead/go inside the hut)?").lower()
        if hut=="move ahead":
          bonus=0
          print("point=",bonus)
          print("You accidently stepped on a a snake so he bite you and you are dead.GAME OVER!.You lost all your points.Better luck next time.")
        elif hut=="go inside the hut":
          bonus=100000
          print("point=",bonus)
          print("Congratulations!.You just found a pot of gold.You are rich now.You earned 100000 points")
          print("You won")
          exit()  
        else:
          print("enter a proper command given in the brackets")

      elif ans=="go around":
        print("You go around and see a tree,you pluck a fruit and eat it.Now a rabbit comes there.")  
        fruit=input("Now do you ignore it or pluck another fruit and offer it to the rabbit?(ignore/pluck)").lower()
        if fruit=="ignore":
          bonus=0
          print("point=",bonus)
          print("You do not have a big heart.The rabbit now turns into a monster and kills you.You loose all your points.GAME OVER.Better luck next time!")  
        elif fruit=="pluck":
          bonus=100000
          print("point=",bonus)
          print("You have a big heart.The rabbit turns into a angel and give you a pot full of gold.congratulations,you are rich now!.You win")
          exit()

        else:
          print("enter a proper command given in the brackets")

    elif direction =="right":
      bonus=0
      print("point=",bonus)
      print("You accidently stepped on a a snake so he bite you and you are dead.GAME OVER!.You lost all your points.Better luck next time.")
      exit()
  else:
    print("Ok,Maybe someother time...BYE!") 
elif age>=14 and age<=18:
  print("You can play with supervision")

else:
  print("Sorry!,you are not old enough to play")  
