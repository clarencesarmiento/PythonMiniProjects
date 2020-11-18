# Let's use our knowledge of number equality to write code that tracks sales data for an online jeans retailer.
# We'll compare jeans_sold with target to see if the retailer hit their sales target.
# Then we'll check if there are jeans still in stock.
# Code a stock variable that stores 600, followed by jeans_sold and target variables that both store 500.
stock = 600
jeans_sold = 500
target = 500
# To see if the sales target was achieved, check if jeans_sold has the same value as target with ==.
# Next, create the variable target_hit to store the result of the comparison.
target_hit = jeans_sold == target
# Display "Hit jeans sale target:".
print("Hit jeans sale target:")
# Finally, use print to display the value of the target_hit variable.
print(target_hit)
# Create current_stock to keep track of the remaining stock.
# Subtract jeans_sold from stock and store the value into current_stock.
current_stock = stock - jeans_sold
# To check if jeans are still in stock, make sure that current_stock not equal to 0.
# Check up on the stock anytime by storing the comparison into the variable in_stock.
in_stock = current_stock != 0
# Finally, display "Jeans in stock", and then on the next line the value of in_stock.
print('Jeans in stock: ')
print(in_stock)
# Good job using number comparisons to keep track of sales data! Hit run to give it another look.
