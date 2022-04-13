import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def convert_to_scientific_notation(input_number):
    value = "{:.2e}".format(input_number)
    return value


#-------------------------------------------------------------------------------
# PART 0: Define global variables
#-------------------------------------------------------------------------------

#np.seterr(divide='ignore', invalid='ignore')

y_axis_title = ['Width(m)']
x_axis_title = ['Length (m)']
graph_title = ['Electric Field Map']

#lengths in cm
x_length = float(input('\nInput length in x-direction (cm): '))
y_length = float(input('Input length in y-directon (cm): '))


#-------------------------------------------------------------------------------
# PART 1: Generate data to make plot
#-------------------------------------------------------------------------------

#Dimension conversion
x_len = x_length/100
x_len_neg = (-1)*(x_len/2)
x_len_pos = x_len/2
y_len = y_length/100

#Coulomb constant (N·(m^2)/(C^2))
k = 8.99*(10**9)

#Charge magnitude (C)
Q = 500*(10**-6)

#Generate grid
x = np.linspace(x_len_neg, x_len_pos, 100)
y = np.linspace(0, y_len, 100)
X, Y = np.meshgrid(x,y)

#Set vectors
rx = x
ry = y

#Calculate distances on grid based on direction vector values
r = []
for y in range(len(ry)):
    rxy = []
    for x in range(len(rx)):
        rxy.append(np.sqrt((rx[x]**2)+(ry[y]**2)))
    r.append(rxy)
r = np.asarray(r)

#Calculate the x,y vectors using the direction vector values
Ex = []
for y in range(len(ry)):
    Exy = []
    for x in range(len(rx)):
        rv = rx[x]
        ro = r[y][x]
        E = ((k*Q)/(ro**2))*(rv/ro)
        if np.isnan(E) == True:
            E = np.nan_to_num(E)
        Exy.append(E)
    Ex.append(Exy)

Ey = []
for x in range(len(rx)):
    Eyx = []
    for y in range(len(ry)):
        rv = ry[y]
        ro = r[x][y]
        E = ((k*Q)/(ro**2))*(rv/ro)
        if np.isnan(E) == True:
            E = np.nan_to_num(E)
        Eyx.append(E)
    Ey.append(Eyx)

Ex = np.asarray(Ex)
Ey = np.asarray(Ey)

#Calculate the magnitudes for each grid location based on the vectors
E = []
for y in range(len(Ey)):
    Exy = []
    for x in range(len(Ex)):
        E_row = np.sqrt((Ex[y][x]**2)+(Ey[y][x]**2))
        Exy.append(E_row)
    E.append(Exy)

E = np.asarray(E)

#print('\nZ-Values:')
Z = E

#-------------------------------------------------------------------------------
# PART 2: Set graph properties
#-------------------------------------------------------------------------------

#Global style parameters
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['axes.linewidth'] = 1.5
mpl.rcParams['font.size'] = 18
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['Tahoma']

#Generate figure object, axes object(s) and set size
#fig, ax = plt.subplots(figsize=(6,4.8))
fig,ax = plt.subplots(figsize=(20,16))

#Generate each individual axis object
#X and Y are for the grid
#Z is for the regions
chart = ax.contourf(X, Y, Z, locator=mpl.ticker.LogLocator(), cmap='coolwarm')

#Set axis labels
ax.set_ylabel(y_axis_title[0], fontsize=24, labelpad=20)
ax.set_xlabel(x_axis_title[0], fontsize=24, labelpad=18)

#Set axis ranges
ax.set_xticks(np.arange(x_len_neg, x_len_pos+0.001, 0.01))
ax.set_yticks(np.arange(0, y_len+0.001, 0.005))

#Set tick styles
ax.tick_params(which='major', length=6, width=1.5)
ax.tick_params(which='minor', length=6, width=1.5)

#Set title
fig.suptitle(graph_title[0], fontsize=28, y=0.97)

#Generate colorbar as legend
legend_colorbar = fig.colorbar(chart, format='%.1e')
legend_colorbar.ax.set_title('E (N/C)', y=1.05)

#Show graph
print('\nGenerating graph...')
plt.show()