import numpy as np
import json
from elo_file import new_rating
from random import randint
import os.path

base = "actor_"

for i in range(300):
	with open (base + str(i) + ".json", "w") as f:
		obj1 = {"info": {"rating": 1500, "username": base + str(i) }, "matches" : []}
		json.dump(obj1, f)