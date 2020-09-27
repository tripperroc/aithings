import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

start_time = time.localtime() 
# Generating artificial data for your example 
# You must use data from your experiment.
dataset = np.random.default_rng().uniform(0,5,(25,4))
dataset[:,0] = range(25)

end_time = time.localtime()

# You need one data for each statistic you measure (fuel left, running time, total time)
# Your dataset should contain one column for each AI agent and one row for each game experiment.
df = pd.DataFrame(dataset, columns=['Game #','Tree Search','Simulated Annealing','Genetic Algorithms'])
df = df.astype(int)

plt.ylabel = ("Fuel Left")
ax = df.plot(x="Game #", y=['Tree Search','Simulated Annealing','Genetic Algorithms'], kind="bar", title="Fuel Remaining at End of Game")
ax.set_ylabel("Fuel Left")
plt.savefig("fuel_left.pdf")
df.to_html("fuel_left.html", index=False)