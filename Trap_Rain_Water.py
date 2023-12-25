“””
If the values are represented by a continuous function instead of discrete points, you would need to integrate the function over the relevant range to determine the volume of trapped water.
Given the continuous function representing the elevation of the roof structure, you can integrate the negative part of the function to find the volume below the roofline. The negative part represents the empty spaces where water can be trapped.
For example, if f(x) represents the elevation function, the volume of trapped water (Vwater) can be calculated as follows:

Here, [a,b] is the range over which you want to calculate the trapped water.
The integral is taken over the region where the function is below the x-axis (negative values). If the function is always non-negative, then there is no trapped water.

To solve the problem where the elevation is represented by a continuous function, you can use calculus to find the area under the curve, which corresponds to the trapped water.
“””

import numpy as np
from scipy.integrate import simps


def trapped_water_continuous(elevation_function, start, end, step=0.001):
   # print(elevation_function,start,step)
   x_values = np.arange(start, end, step)
   print(x_values)
   y_values = [elevation_function(x) for x in x_values]
   # print(y_values)
   min_elevation = min(y_values)
   print(min_elevation)
   adjusted_heights = [max(elev - min_elevation, 0) for elev in y_values]


   trapped_water = simps(adjusted_heights, dx=step)
   return trapped_water


# Example: Quadratic function representing a roof structure
def quadratic_elevation(x):
   return (x)**2


start_position = 0
end_position = 10


result = trapped_water_continuous(quadratic_elevation, start_position, end_position)
print(f"Estimated trapped water: {result} square units")