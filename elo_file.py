import  numpy as np 

def new_rating(R1: float, R2: float, res_1: bool, res_2: bool):
	
	#K factor should be a function of the difference and number of matches played, perhaps? Maybe included as a volatility parameter
	k = 32

	Q1 = 10**(R1/400.)
	Q2 = 10**(R2/400.)

	Q_sum = Q1 + Q2
	E1 = Q1/Q_sum
	E2 = Q2/Q_sum

	if res_1 + res_2 == 2:
		S1 = 0.5
		S2 = 0.5
	else:
		S1 = 1*res_1
		S2 = 1*res_2

	new_R1 = R1 + k*(S1 - E1)
	new_R2 = R2 + k*(S2 - E2)

	return new_R1, new_R2 


