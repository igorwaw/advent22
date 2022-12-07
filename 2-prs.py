#!/usr/bin/python3


INPUTFILE="2-input.txt"

scoreshape={'ROCK':1, 'PAPER':2, 'SCISSORS':3}
scoreoutcome={'LOST':0, 'DRAW':3, 'WON':6}

opp_card={'A':'ROCK', 'B': 'PAPER', 'C':'SCISSORS'}
my_card={'X':'ROCK', 'Y': 'PAPER', 'Z':'SCISSORS'}

gamescore=0
numrounds=0
with open(INPUTFILE) as inputfile:
	for line in inputfile:
		opponent,me=line.split()
		roundscore=0
		outcome=None
		match me:
			case 'X':
				roundscore=scoreshape['ROCK']
				if opponent=='A':
					outcome='DRAW'
				elif opponent=='B':
					outcome='LOST'
				elif opponent=='C':
					outcome='WON'
				else:
					raise(ValueError)
			case 'Y':
				roundscore=scoreshape['PAPER']
				if opponent=='B':
					outcome='DRAW'
				elif opponent=='C':
					outcome='LOST'
				elif opponent=='A':
					outcome='WON'
				else:
					raise(ValueError)
			case 'Z':
				roundscore=scoreshape['SCISSORS']
				if opponent=='C':
					outcome='DRAW'
				elif opponent=='A':
					outcome='LOST'
				elif opponent=='B':
					outcome='WON'
				else:
					raise(ValueError)					
			case _:
				raise(TypeError)
		roundscore=roundscore+scoreoutcome[outcome]
		gamescore=gamescore+roundscore
		numrounds=numrounds+1
		print("Round:",numrounds, ', opponent:', opp_card[opponent], \
		    ', me:', my_card[me], ', outcome:', outcome, \
		    ', round score: ', roundscore)

print("------------------------------")
print("Number of rounds: ",numrounds, ", total score: ", gamescore)

