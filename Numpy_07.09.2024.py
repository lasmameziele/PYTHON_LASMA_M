import numpy as np
import matplotlib.pyplot as plt

num_trials = 700 

outcomes = {'HH': 0, 'HT': 0, 'TH': 0, 'TT': 0} #This is dictionary to count outcomes

for _ in range(num_trials):
    coin1 = np.random.choice(['H', 'T'])  # Toss coin 1
    coin2 = np.random.choice(['H', 'T'])  # Toss coin 2
    outcome = coin1 + coin2  # Combine results
    outcomes[outcome] += 1  # Count the outcome

# Here we calculate probabilities
probabilities = {outcome: count / num_trials for outcome, count in outcomes.items()}

my_colors = ['yellow', 'pink', 'purple']

plt.figure(figsize=(7, 7)) #Create the plot

# Draw each bar with multiple colors
for outcome, probability in probabilities.items():
    segment_height = probability / len(my_colors)  # Height of each color segment
    
    for j, color in enumerate(my_colors):
        plt.bar(outcome, segment_height, bottom=j * segment_height, color=color, edgecolor='none') #Draw a bar segment with color.

plt.title('Probabilities of Outcome')
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.ylim(0, 1)  # Set y-axis limits
plt.grid(axis='y', linestyle='solid', color='yellow', alpha=0.8)  # Add grid
plt.show()  # Display the plot

print('Calculated Probabilities:')
for outcome, prob in probabilities.items():
    print(f'The outcome {outcome} is with probability {prob:.2f}')
