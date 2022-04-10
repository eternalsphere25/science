from scipy.constants import Avogadro
import scipy as sp
import random
import math

def calculate_step_length(input_element, input_energy):
    #Select element and return element parameters
    element = input_element

    #Input energy
    E = input_energy

    #Calculate mean free path
    a = (3.4*10**-3)*(element.z)**(0.67)/E

    #Calculate total screened Rutherford elastic cross section
    sigma = (
        (5.21*10**-21)*(element.z)**2/E**2*(
            4*sp.pi/(a*(a+a)))*((E+511)/(E+1024))**2)

    #Calculate mean free path
    lambda_calc = (element.amu)/(Avogadro*(element.density)*sigma)

    #Calculate step length using a random number
    s = (-1)*lambda_calc*math.log(random.random())

    return s