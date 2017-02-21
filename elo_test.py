import numpy as np 
from elo_file import new_rating

R1 = 1500
R2 = 1500 

a, b = new_rating(R1, R2, True, False)

print(a, b)