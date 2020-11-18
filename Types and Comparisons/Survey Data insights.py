# Let's use string comparisons to label data acquired through a fitness app's user survey.
# We'll check the users' survey answers to regarding activity frequency and intensity,
# label them, and display the results.
# The current user does sports once a week, so create a frequency variable set to "once a week".
frequency = 'once a week'
# Next, save the user's answer regarding sports intensity into an intensity variable set to "low".
intensity = 'low'
# To label a user as highly active, we need to check if frequency equals "daily".
# Create the variable highly_active to save the result of the comparison.
highly_active = frequency == 'daily'
# Next, display "Highly active user:" in the console.
print('Highly Active User: ')
# Finally, display the value of highly_active.
print(highly_active)
# To label the user as doing high-intensity sports, check if the variable intensity equals "high".
# Create the variable high_intensity to save the result of the comparison.
high_intensity = intensity == 'high'
# Next, display "High intensity sports:" in the console.
print('High Intensity User: ')
# Finally, display the value of the high_intensity variable.
print(high_intensity)
# Good job using string comparisons to label survey data and gain insights about the fitness app's users!