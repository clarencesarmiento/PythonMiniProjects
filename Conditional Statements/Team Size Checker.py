# Chapter 1: Checks if the teams have the same number of players
# Let's use conditionals and list length to check team sizes and decide on the number of rounds left in a game.
# We'll store the two teams in a list, check if they have the same length,
# then display the rounds left based on the length.
# Create the list team_1 that stores three players.
team_1 = ['Mia', 'Lexi', 'Rachelle']
# Finish coding the second team's list, by adding James, followed by Ty, and then Ava.
team_2 = ['James', 'Ty', 'Ava']
# For the size of the first team, create the variable size_1 that stores the length of team_1.
size_1 = len(team_1)
# Like before, create a variable size_2 and use len() to store the size of team_2 in it.
size_2 = len(team_2)
# To see if the teams have different sizes, code an if statement that checks if size_1 is not equal to size_2.
if size_1 != size_2:
    # If the team sizes are different, display a warning.
    print('Teams must have the same size!')
# In case the teams have the same size, code an else statement.
else:
    # For same-sized teams, display "Game on!" in the console.
    print('Game on!')

# Chapter 2: Calculating the rounds left
# Now that we know that the teams have the same size, we can decide how many rounds they can play based on their size.
# Code an if statement that checks if size_1 is equal to 3.
if size_1 == 3:
    # For teams of size three, display "Rounds left: 3" in the console.
    print('Rounds Left: 3')
# Next, code an elif statement that checks if size_1 is equal to 2.
elif size_1 == 2:
    # For two-player teams, display "Rounds left: 2".
    print('Rounds Left: 2')
# For the only option left, single-player teams, code an else statement.
else:
    # If only one player is left in each team, display "Final round!".
    print('Final Round!')
# Done! You've used conditionals together with the list length instruction to check for invalid team sizes
# and decide on the next round.
