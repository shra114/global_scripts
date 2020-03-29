#Swiss pairing program:
from operator import add
import random


num_players = 44
player_names = ["p"+str(i) for i in range(num_players)]
rounds = 6
player_opponents = dict()
player_scores = dict()
player_scorecard = dict()


def get_player_sorted(scores_dict):
	sorted_scores = (sorted(scores_dict.items(), key = lambda kv:(kv[1], kv[0]))) 
	players = list()
	print "--------Sorted list------------"
	for i in  sorted_scores[::-1]:
		print i
	for i in sorted_scores:
		players.append(i[0])
	return players[::-1]

for i in range(num_players):
	player_opponents["p"+str(i)] = list()
	player_scores["p"+str(i)] = i%7  #Edit this if player scores are available
	player_scorecard["p"+str(i)] = [0,0,0,0]  #win lose draw score
print player_names
print player_opponents
print player_scores


	
sorted_players =  get_player_sorted(player_scores)
#print get_player_sorted(player_scores)

for i in range(rounds):
	#initial values
	remaining_list = sorted_players
	paired_players = list()
	pairs = list()
	print "Paring for round ",i
	for player1 in sorted_players:
		if player1 not in paired_players:
			paired_players.append(player1)
			for player2 in sorted_players[sorted_players.index(player1)+1:]: #start from the guys below him
				#what if he is already paired_players with other player
				if (player2 in paired_players):
					continue
				if(player2 not in player_opponents[player1]):
					paired_players.append(player2)
					player_opponents[player1].append(player2)
					player_opponents[player2].append(player1)
					break
			pairs.append((player1, player2))
	
	#Pairing
	print "==="*10
	for j in pairs:
		print j
		
	#Results
	print "Results after round ", i
	for j in pairs:
		result = random.choice(range(1000))%2 #player1 win lose draw
		if result == 0: 
			player_scorecard[j[0]] = list(map(add, player_scorecard[j[0]], [1,0,0,2]))
			player_scorecard[j[1]] = list(map(add, player_scorecard[j[1]], [0,1,0,0]))
		if result == 1:
			player_scorecard[j[0]] = list(map(add, player_scorecard[j[0]], [0,1,0,0]))
			player_scorecard[j[1]] = list(map(add, player_scorecard[j[1]], [1,0,0,2]))
		if result == 2:
			player_scorecard[j[0]] = list(map(add, player_scorecard[j[0]], [0,0,1,1]))
			player_scorecard[j[1]] = list(map(add, player_scorecard[j[1]], [0,0,1,1]))
	
	for j in player_scorecard:
		print j,player_scorecard[j]
	
	for j in player_scores:
		player_scores[j]= player_scorecard[j][3]
	sorted_players =  get_player_sorted(player_scores)
