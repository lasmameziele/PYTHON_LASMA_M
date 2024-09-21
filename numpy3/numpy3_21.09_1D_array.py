import numpy as np

position = 0
total_steps = 0
up_steps = 0


while True:
    step = np.random.choice([-1, 1]) 
    position += step  # Update 
    total_steps += 1  # Increment

    # Count upward steps
    if step == 1:
        up_steps += 1

    # Condition to stop 
    if abs(position) >= 777:
        break

print(f'Total steps: {total_steps}')
print(f'Upward steps: {up_steps}')
print(f'My current position: {position}')


plt.plot(positions, label='Position', color='green')
plt.title('1D Random Walk')
plt.xlabel('Steps')
plt.ylabel('Position')
plt.axhline(0, color='black', lw=0.8, ls='--')  # Line at y=0 for reference
plt.grid()
plt.legend()
plt.show()
