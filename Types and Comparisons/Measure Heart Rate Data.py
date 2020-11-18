# Let's create a program that analyzes a patient's heart rate.
# We'll use comparisons to check if the heart rate is too low or too high
# and tell the patient if they should worry about their health.
# Create a heart_rate variable. It'll store the heart rate from the heart rate sensor.
# Set the heart_rate variable to a number so we can compare it to other numbers.
heart_rate = 77
# Create a too_low variable. We'll use it to tell us if a heart rate is too low.
# Now check if heart_rate is less than 60 and store the result in too_low.
too_low = heart_rate < 60
# Create a too_high variable. We'll use it to tell us if a heart rate it's too high.
# Now use > to check if heart_rate is greater than 100.
too_high = heart_rate > 100
# We'll tell the patient if their heart rate is too low. Start by displaying Heart rate low: in the console.
print('Heart Rate Low: ')
# Now display the value of too_low in the console.
print(too_low)
# We'll also tell the patient if their heart rate is too high. Display Heart rate high: in the console.
print('Heart Rate High: ')
# Now display the value of too_high in the console.
print(too_high)
# You've built a neat little program that checks if a heart rate is too low or too high.
