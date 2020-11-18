# Chapter 1: Largest
# Let's use our knowledge of lists to analyze an unsorted dataset of the ten largest lakes in the United States.
# We'll use max() and min() to find the dataset's largest and smallest values.
# Then, we'll display the difference between them.
# Create a list to hold the sizes of the biggest lakes in the United States in square meters.
sizes = [7340, 2117, 22300, 31700, 1679, 1014, 23000, 9910, 685]
# We'll find the largest lake in the list first. Code largest as the name of the variable we'll use.
# Use max() to find the largest value in the list and assign it to largest.
largest = max(sizes)
# Add an empty print() statement that we'll use for displaying the value.
print('Largest lake in sq mi:')
print(largest)
# Chapter 2: Smallest
# Now it's time to find the smallest lake in the dataset.
# Create a new variable and use min() to retrieve and store the smallest value.
smallest = min(sizes)
# Display statement for the tenth biggest lake.
print('10th largest lake in sq mi:')
# Display the smallest variable in the console.
print(smallest)
# Let's find out the difference in size between both lakes by subtracting
# smallest from largest and storing the result in difference.
difference = largest - smallest
# Display the difference between lakes
print('Difference between lakes in sq mi')
# Finally, display the difference variable in the console.
print(difference)
# There we have it! We've used some built-in Python functionality to find
# the largest and smallest values in an unsorted dataset
