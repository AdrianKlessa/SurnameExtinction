import numpy as np
import matplotlib.pyplot as plt

start = 300 #How many people with that surname we start with

number_of_generations = 100 #how long the simulation lasts
number_of_reruns=1000 # how many times we simulate it

sizes = np.zeros([number_of_reruns,number_of_generations+1], dtype=int)
sizes[:,0]=start

for rerun in range(number_of_reruns):
    for generation in range(1,number_of_generations):
        values = np.random.choice(a=[0,1,2,3], size=sizes[rerun,generation-1], p=[0.48,0.41,0.1,0.01])
        sizes[rerun,generation]=np.sum(values)

print("Sizes:")
print(sizes)
#Average size of each generation
average_sizes = sizes.mean(axis=0)

print("Averages of each generation:", average_sizes)

#Number of extinctions
last_gen = sizes[:,-1]
extinctions = np.sum(last_gen==0)
print("Number of extinctions: ",extinctions)
print("Estimated probability of extinction: ",extinctions/number_of_reruns)

for x in range(number_of_generations):
    data = sizes[:,x]
    fig, ax = plt.subplots()
    ax.hist(data)
    ax.set_title("Size distribution for generation "+(str)(x))
    fig.savefig("Size distribution for generation "+(str)(x))
    
plt.plot(sizes[0,:])
plt.show()

