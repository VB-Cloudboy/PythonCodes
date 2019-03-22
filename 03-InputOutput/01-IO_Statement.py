# A series of Input-Output Statement

#01-Playing with String
player = str(input("Enter a Player Name: "))
print('you just wrote: ', player)

#02-Playing with Numbers
player = int(input("Enter a Player Jersey Number: "))
print('you just wrote: ', player)

#03-Palying with Multiple Numbers
batsmen01 = str(input("Enter Player01 name: "))
batsmen02 = str(input("Enter Player02 name: "))
play01 = int(input("Enter a player jersey number: "))
play02 = int(input("Enter a player jersey number: "))
print("Please do not opt for {} and {} numbers".format(play01,play02))

#03-Floating with Numbers
exp = float(input("What's the ICC cost of the player ? = "))
print("The Player cost is ", exp)

#04-Split fucntion with commas
num1, num2, num3 = [int(x) for x in input("Enter the player jersey number: ").split()]
print("The sum goes to = ", num1+num2+num3)
dname = [x for x in input("Please enter your Full-Name: ").split(',')]
print('Your full name: \n', dname)

#05-List & Tuple as an IO
lst = eval(input("Enter the players name: "))
print("List = ", lst)
tpl = eval(input("Enter a jersey numbers of players: "))
print("Tuple= ", tpl)



