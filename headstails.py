import random

# You go to a casino and play a brand new game where they flip two hidden coins, and then you place a bet. 
# They tell you honestly, "one of the coins came up heads, do you want to bet the other coin is heads or tails?" 
# However if both coins had come up tails, they don't say anything, your bet is simply refunded. 
# It turns out that, after playing many games, you would lose money betting heads, and you would win money by betting tails. 


def play_game1(bet_on, bet_amt, n):
	pot = 0
	for i in range(n):
		coin1 = random.choice(["Heads", "Tails"])
		coin2 = random.choice(["Heads", "Tails"])
		# We bet on the other coin after both are flipped
		pot -= bet_amt
		if coin1 == "Tails" and coin2 == "Tails":
			pot += bet_amt  # refund
			continue  # skip tails-tails
		if bet_on == "Heads" and coin1 == "Heads" and coin2 == "Heads" or bet_on == "Tails" and (coin1 == "Tails" or coin2 == "Tails"):
			pot += bet_amt + bet_amt
	return pot

# This casino also offers a similar game where the only difference is that they flip the coins one at a time. 
# You bet on the outcome of the yet-to-be-flipped coin after one coin has already landed on heads or tails. 
# Just like in the first game, if the coins come up tails-tails, the casino will issue a refund. What has changed? 
# Now it makes the most sense to always bet heads!

def play_game2(bet_on, bet_amt, n):
	pot = 0
	for i in range(n):
		coin1 = random.choice(["Heads", "Tails"])
		# We bet on the second coin before it is flipped.
		pot -= bet_amt
		coin2 = random.choice(["Heads", "Tails"])
		if coin1 == "Tails" and coin2 == "Tails":
			pot += bet_amt  # refund
			continue
		if bet_on == coin2:
			pot += bet_amt + bet_amt
	return pot

# In another game, the dealer either tells you that the coin landed on heads or tails.
# Then you bet on the other coin. No outcomes are refunded.

def play_game3(bet_on, bet_amt, n):
	pot = 0
	for i in range(n):
		coin1 = random.choice(["Heads", "Tails"])
		coin2 = random.choice(["Heads", "Tails"])
		# We bet on the other coin after both are flipped
		pot -= bet_amt
		reveal = random.choice([coin1, coin2])
		if (coin1 == reveal and coin2 == bet_on or coin1 == bet_on and coin2 == reveal):
			pot += bet_amt + bet_amt * 0.99
	return pot

# The fourth game, is like the 3rd game, except the dealer has a bias towards calling heads.

def play_game4(bet_on, bet_amt, n):
	pot = 0
	for i in range(n):
		coin1 = random.choice(["Heads", "Tails"])
		coin2 = random.choice(["Heads", "Tails"])
		# We bet on the other coin after both are flipped
		pot -= bet_amt
		reveal = "Heads"
		if coin1 == "Tails" and coin2 == "Tails":
			reveal = "Tails"
		if (coin1 == reveal and coin2 == bet_on or coin1 == bet_on and coin2 == reveal):
			pot += bet_amt + bet_amt * 0.99
	return pot

if __name__ == "__main__":
	n = 100000
	bet_amt = 1
	print("Game1: Betting on Heads (unfavorable):", play_game1("Heads", bet_amt, n))
	print("Game1: Betting on Tails (favorable):", play_game1("Tails", bet_amt, n))
	print("Game2: Betting on Heads (favorable):", play_game2("Heads", bet_amt, n))
	print("Game2: Betting on Tails (unfavorable):", play_game2("Tails", bet_amt, n))

	print("Game3: Betting on Heads (?):", play_game3("Heads", bet_amt, n))
	print("Game3: Betting on Tails (?):", play_game3("Tails", bet_amt, n))
	print("Game4: Betting on Heads (unfavorable):", play_game4("Heads", bet_amt, n))
	print("Game4: Betting on Tails (favorable):", play_game4("Tails", bet_amt, n))
