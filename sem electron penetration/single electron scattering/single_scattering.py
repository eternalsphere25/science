import step_length
import element_data
import final_energy
import next_point
import matplotlib.pyplot as plt

#Set element
element = element_data.lookup_element(input('\nInput element symbol: '))

#Set energy
E = float(input('Input energy: '))

#Set 2D or 3D output
print('\nSet graphical output:')
print("2D: '2'")
print("3D: '3'")
graph_output = int(input('Input: '))

#Calculate initial step length
initial_step_length = step_length.calculate_step_length(element, E)

#Initial points and angles (initial penetration depth)
x = [0,0]
y = [0,0]
z = [0, initial_step_length]
cx = [0,0]
cy = [0,0]
cz = [1,1]

En = final_energy.calculate_final_energy(element, E, z[1])
E = En
count = 1

#Electron continues to travel while energy is > 50eV (0.05 keV)
while E >= 0.05 and z[-1] >= 0:
    #Find step length
    s = step_length.calculate_step_length(element, E)

     #Find next point
    next_point_data = next_point.calculate_next_point(
        element, E, s,
        x[count], y[count], z[count],
        cx[count], cy[count], cz[count]
        )

    #Add next point data to coordinate vectors
    x.append(next_point_data[0])
    y.append(next_point_data[1])
    z.append(next_point_data[2])
    cx.append(next_point_data[3])
    cy.append(next_point_data[4])
    cz.append(next_point_data[5])

    #Calculate final energy
    En - final_energy.calculate_final_energy(element, E, z[count+1])
    E = En

    count += 1

#print(x)
#print(y)
#print(z)
#print(cx)
#print(cy)
#print(cz)

#Graph results
if graph_output == 2:
    fig, ax = plt.subplots()
    ax.plot(x, z)
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_axisbelow(True)
    ax.set_ylim(-max(z))
    ax.invert_yaxis()
    plt.show()

elif graph_output == 3:
    ax = plt.axes(projection='3d')
    ax.plot3D(x, y, z)
    ax.scatter(0, 0, 0, c='red')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    plt.show()