# Chapter 1: Creating variables
# Let's use our knowledge of while loops to see how the amount stored in a bank account
# increases over time, with a given interest rate.
# We'll store the initial amount, interest rate, and time span in variables.
# Then, in a loop, increase the account by the interest rate.
# Start by creating the variable account set to 100, to store the initial amount.
account = 100
# We'll store the yearly interest rate by setting the variable interest_rate to the percentage value 0.004.
interest_rate = 0.004
# We want to calculate how our initial amount grows over three years, so code the variable years set to 3.
years = 3
# Before we jump to calculations, let's use an f-string and the variable account to display Initial amount: 100.
print(f'Initial Amount: {account}')
# To increase the account for each year, we'll need a loop.
# Start by coding a counter variable set to 1, for the first year.
counter = 1
# Code the keyword that starts a while loop.
# Choose a condition that makes the loop run three times, once for each year. Then, finish with a colon :.
while counter <= years:
    # Chapter 2: Making Calculation
    # The interest rate tells us the percentage of our yearly accrued interest.
    # We calculate this amount by multiplying account by the interest_rate percentage.
    # Code the variable accrued_interest, multiply account by interest_rate, and store the result in the variable.
    accrued_interest = account * interest_rate
    # To update account to its value plus that of accrued_interest, use self-assignment.
    account += accrued_interest
    # Check how the capital increases by displaying the f-string f"year {}: {}" with counter
    # and account between the curly braces.
    print(f'Year {counter}: {account}')
    # Finally, use self-assignment to increase the counter by one.
    counter += 1
# Well done increasing the capital in a while loop,
# then using a counter to stop it after three years. Run the code to give it another look.
