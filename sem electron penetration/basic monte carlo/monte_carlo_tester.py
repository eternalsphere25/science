import numpy as np
import matplotlib.pyplot as plt
import monte_carlo_2d


#----------------------------------------
#Set variables
#----------------------------------------

#Number of iterations at that number of steps
num = 10

#Number of steps
steps = [100, 200, 300, 400, 500, 600, 700, 800]

#Distance from origin
dist = np.zeros((num*len(steps), 2))

#Counter
count = 0

#Average distance
m = np.zeros((len(steps), 1))


#----------------------------------------
#Iterate over different number of steps a total of num times to determine the 
#average and compare to the theoretical
#----------------------------------------

for i in range(len(steps)):
    for k in range(num):
        dist[count][0] = steps[i]
        dist[count][1] = monte_carlo_2d.monte_carlo_2d(steps[i])[2]
        count += 1
    m[i] = np.average([dist[x][1] for x in range(count-num, count-1)])


#Calculate theoretical values
theoretical_x = np.linspace(0, 800, 100)
theoretical_y = np.sqrt(theoretical_x)


#----------------------------------------
#PLot results
#----------------------------------------

#Generate graph
fig, ax = plt.subplots()

#Plot theoretical value
ax.plot(theoretical_x, theoretical_y, color='green', linestyle='--')

#Plot actual values
ax.scatter(dist[:,0], dist[:,1], color='blue', facecolors='none', edgecolors='blue')

#Plot averages of the actual values
ax.scatter(steps, m, color='red')

#Set axis labels
ax.set_xlabel('Steps')
ax.set_ylabel('Distance From Origin (Steps)')

#Set legend
ax.legend(['Theoretical', 'Distance', 'Mean Distance'])

#Show plot
plt.show()