# To calculate state value functions iteratively.
states = ['C1', 'C2', 'C3', 'FH', 'PASS', 'NF', 'TERMINATE']  # Defining the states
# State Transition Matrix.
p = [[0, .5, 0, 0, 0, .5, 0],
     [0, 0, .8, 0, 0, 0, .2],
     [0, 0, 0, .4, .6, 0, 0],
     [.2, .4, .4, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1],
     [.1, 0, 0, 0, 0, .9, 0],
     [0, 0, 0, 0, 0, 0, 1]]
r = [-2, -2, -2, 1, 10, -1, 0]  # Reward Matrix.
v_s, v_s_next = r, list()
gamma = .9  # Discount Factor
count = 1
while 1:
    for i in range(7):
        v_s_next.append(r[i]+gamma*sum([p[i][j]*v_s[j] for j in range(7)]))  # Bellman Equation
    if abs(v_s_next[0] - v_s[0]) <= 1e-3:
        break
    v_s = v_s_next
    v_s_next = list()
    for i in range(7):
        print('The state value function of state {:} after iteration {:} is {:}.'.format(states[i], count, v_s[i]))
    count += 1
# C1=-5.01,C2=.94,C3=4.09,FH=1.91,PASS=10,NF=-7.64,T=0.(Final State Value Functions)
