# WAP to Store two points as tuples and calculate distance

import math

p1 = (2, 3)
p2 = (6, 7)

distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

print("Distance:", distance)