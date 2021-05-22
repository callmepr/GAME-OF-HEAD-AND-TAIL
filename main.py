import random,time

coin = ['HEAD', 'TAIL']

while True:
  print("\n Lets play Game of HEAD AND TAIL")
  print("\n1.HEAD \n2.TAIL")
  any = random.choice(coin)

  try:
    option = int(input("Enter the option between 1 & 2, \n Your Selection: "))
  except:
    print("\nYou have not selected the option from the given ..")
    continue

  if option == 1:    
    print("\nLooks like u are winning the game..")
    time.sleep(3)
    if any == 'HEAD':
      print("\nCongrats,Give a party to your all College Friend. You have won the game..")
    else:
      print("\nYou Lost, Better Luck Next Time.")
    print('Umpire call:-', any)

  elif option == 2:
    print("\nLooks like u are winning the game..")
    time.sleep(3)
    if any == 'TAIL':
      print("\nCongrats,Give a party to your all College Friend. You have won the game..")
    else:
      print("\nYou Lost, Better Luck Next Time.")
    print('Umpire call:-', any)
    
  else:
    print("\nYou have not selected the option from the given ..")

  print("\n----------------made by-Rupesh Prajapati\nfollow on instagram @rupesh_pr7 ----------------")#keep supporting
