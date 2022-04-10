import math

def calculate_final_energy(input_element, input_energy, input_step_length):

    #Set element
    element = input_element

    #Set energy
    E = input_energy

    #Set step length
    s = input_step_length

    #Calculate mean ionization potential
    J = (9.76*(element.z)+58.5/(element.z)**0.19)*10**-3

    #Modified version of the Bethe equation
    dEdS = -78500*(element.z)/((element.amu)*E)*math.log(1.166*(E+0.85*J)/J)

    #Final energy
    En = E + s*(element.density)*dEdS

    return En