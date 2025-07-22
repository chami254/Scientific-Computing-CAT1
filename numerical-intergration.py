#program to calculate the volume under the surface z = x2+y2 over the square region 0 ≤ x, y ≤ 1 

import scipy.integrate as integrate

# Define the function z = x^2 + y^2
def integrand(y, x):
    return x**2 + y**2

# Integration bounds for x and y: 0 to 1
result, error = integrate.dblquad(integrand, 0, 1, lambda x: 0, lambda x: 1)

print("Volume under the surface z = x^2 + y^2 over [0,1]x[0,1] is:", result)
