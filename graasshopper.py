import numpy as np 

num_states = 101          #number of discrete state points
jump_range = 20           #jump range 



tp = []                   #tansition probability matrix

for i in range (0,num_states,1):
	if i + jump_range > num_states - 1:
		upper = num_states - 1
	else:
		upper = i + jump_range

	if i - jump_range < 0:
		lower = 0
	else:
		lower = i - jump_range

	p = 1/(upper - lower)	
	tp.append([])

	for j in range (0, num_states,1):
		if abs(j-i) > jump_range or j == i:
			tp[i].append(0)
			
		else:
			tp[i].append(p)


# solving the steady state equation


p_hat = tp.copy()


for i in range(0,num_states,1):
	p_hat[i].pop()

b = p_hat.pop()

 
identity = np.identity(num_states-1)

i_p = identity - p_hat

i_p_inv = np.linalg.inv(i_p)

pi_hat = np.dot(b,i_p_inv)


c = 1 

for i in pi_hat:
	c += i 

pi = []       # this is the vector of final solution probabilities


for i in pi_hat:
	pi.append(i/c)

pi.append(1/c)

# print out steady state state probabilities
for i in pi:
	print(i)
