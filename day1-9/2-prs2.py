#!/usr/bin/python3


INPUTFILE="2-input.txt"

scoreshape={'ROCK':1, 'PAPER':2, 'SCISSORS':3}
scoreoutcome={'LOST':0, 'DRAW':3, 'WON':6}

name_cards={'A':'ROCK', 'B': 'PAPER', 'C':'SCISSORS'}
my_card={'X':'LOST', 'Y': 'DRAW', 'Z':'WON'}

gamescore=0
numrounds=0
with open(INPUTFILE) as inputfile:
	for line in inputfile:
		opponent,me=line.split()
		roundscore=0
		play=None
		outcome=my_card[me]
		match outcome:
			case 'LOST':
				if opponent=='A':
					play='C'
				elif opponent=='B':
					play='A'
				elif opponent=='C':
					play='B'
				else:
					raise(ValueError)
			case 'DRAW':
				play=opponent
			case 'WON':
				if opponent=='A':
					play='B'
				elif opponent=='B':
					play='C'
				elif opponent=='C':
					play='A'
				else:
					raise(ValueError)
			case _:
				raise(TypeError)
		roundscore=scoreoutcome[outcome]+scoreshape[name_cards[play]]
		gamescore=gamescore+roundscore
		numrounds=numrounds+1
		print("Round:",numrounds, ', opponent:', name_cards[opponent], \
		    ', outcome:', my_card[me], ', me:', name_cards[play], \
		    ', round score: ', roundscore)

print("------------------------------")
print("Number of rounds: ",numrounds, ", total score: ", gamescore)

