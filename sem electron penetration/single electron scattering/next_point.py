import random
import math

def calculate_next_point(
    input_element, input_energy, step_length,
    x, y, z,
    cx, cy, cz
    ):

    #Set screening factor
    a = (3.4*10**-3)*(input_element.z)**(0.67)/input_energy

    #Calculate random new angles
    num = random.random()
    cphi = 1-2*a*num/(1+a-num)
    sphi = math.sqrt(1-cphi**2)
    psi = 2*math.pi*random.random()

    #Calculate next point info from equations given in Joy book
    am = -(cx/cz)
    an = 1/math.sqrt(1+am**2)

    v1 = an*sphi
    v2 = an*am*sphi
    v3 = math.cos(psi)
    v4 = math.sin(psi)

    #New cosine angles
    ca = cx*cphi+v1*v3+cy*v2*v4
    cb = cy*cphi+v4*(cz*v1-cx*v2)
    cc = cz*cphi+v2*v3-cy*v1*v4

    #New point coordinates
    xn = x + step_length*ca;
    yn = y + step_length*cb;
    zn = z + step_length*cc;

    return xn, yn, zn, ca, cb, cc