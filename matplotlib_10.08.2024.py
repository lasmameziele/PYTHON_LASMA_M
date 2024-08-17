import pandas as pd
import matplotlib.pyplot as plt
pokemon_df=pd.read_csv('/content/Pokemon.csv')
pokemon_df.head(n=7)

plt.hist(pokemon_df['Speed'], color='yellow', edgecolor='green', bins=10)
plt.xlabel('Speed')
plt.ylabel('Frequency')
plt.title('Distribution of Pokemon Speed')

plt.axvline(pokemon_df['Speed'].median(), color='red', linestyle='dotted', linewidth=2)
plt.axvline(pokemon_df['Speed'].min(), color='blue', linestyle='dotted', linewidth=2) 
plt.axvline(pokemon_df['Speed'].max(), color='green', linestyle='dashed', linewidth=2)
plt.show()

--Correlation: positive colleration means if attach increasers, also defense increases.
#Scatterplot
plt.scatter(pokemon_df['Attack'], pokemon_df['Defense'], color='red', alpha=0.5)






