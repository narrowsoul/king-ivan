# King Ivan boss fight simulation
# Princes Dmitry and Feodor

## --------------------------------
## Definitions of all the players and constants will go here, probably stored in arrays
## with health, DPS, healing ability or whatever else
## Mess with variables here to change the parameters of the simulation

# Ivan's values
IVAN_MAXHP = 50000
IVAN_DPS = 1000
IVAN_TARGET = 4
IVAN_HEAL = 0
# Dmitry's values
DMITRY_MAXHP = 2000
DMITRY_DPS = 250
DMITRY_TARGET = 1
DMITRY_HEAL = 0
# Feodor's values
FEODOR_MAXHP = 2000
FEODOR_DPS = 250
FEODOR_TARGET = 1
FEODOR_HEAL = 0

# Char definition: [Health, DPS, Players hit per strike, Healing per turn]
ivan = [IVAN_MAXHP, IVAN_DPS, IVAN_TARGET, IVAN_HEAL]
dmitry = [DMITRY_MAXHP, DMITRY_DPS, DMITRY_TARGET, DMITRY_HEAL]
feodor = [FEODOR_MAXHP, FEODOR_DPS, FEODOR_TARGET, FEODOR_HEAL]

thomas = [3000, 200, 1, 0] # Tank
diana = [1500, 500, 1, 0] # DPS Fighter
winry = [1000, 500, 2, 0] # Warlock
harry = [1500, 300, 1, 250] # Healer

# Various variables to determine outcome
PRINCE_RESPAWN_CHANCE = 80

## --------------------------------
# Definitions of all other required variables

princeCount = 2 # Number of princes alive
diceRoll = 1 # d100 dice roll

## --------------------------------
# Definitions of functions such as attacks, script to 
# spawn princes, randomize targets, etc


# Random number generator
def d100():
	"Return an integer from 1-100"
	import random
	x = random.randrange(1,100,1)
	return x

# Prince spawn
def princeSpawn (princeCount):
	"Chance to spawn a new prince if one of them is dead"
	if princeCount < 2:
		diceRoll = d100()
		if dmitry[0] <= 0 and diceRoll > PRINCE_RESPAWN_CHANCE:
			dmitry[0] = DMITRY_MAXHP
			princeCount += 1
		diceRoll = d100()
		if feodor[0] <= 0 and diceRoll > PRINCE_RESPAWN_CHANCE:
			feodor[0] = FEODOR_MAXHP
			princeCount += 1
		
		
## --------------------------------

# Main function

diceRoll = d100()
print(diceRoll)
for x in range (0,50):
	print("Turn Start")
	print(princeCount)
	if dmitry[0] > 0:
		dmitry[0] = 0
		princeCount -= 1
	princeSpawn(princeCount)
	print("Turn End")
	print(princeCount)
	x += 1