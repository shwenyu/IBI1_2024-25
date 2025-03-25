import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rdm
Pop = 10000 # can be changed into an input 
Inf = 1 # Infecrd people
Sus = Pop-1 # Suspectible people
Rec = 0 # Recovered people
beta = 0.3 # the basic infection rate and should be mutiplied by proportion of the infected when to  calculated the infection rate with infected people
gamma = 0.05 # the recovery rate 
Track_s = [] # store the arrays
Track_s.append(Sus)
Track_i = []
Track_i.append(Inf)
Track_r = []
Track_r.append(Rec)
recursion_time = 1000 # can be changed
# the loop
for i in range(recursion_time):
    Sus2Inf_rate = beta * (Inf/Pop)
    Inf2Rec_rate = gamma
    Sus2Inf = sum(rdm.choice(range(2),Sus,p=[1-Sus2Inf_rate,Sus2Inf_rate]))
    Sus2Sus = Sus - Sus2Inf
    Inf2Rec = sum(rdm.choice(range(2),Inf,p=[1-Inf2Rec_rate,Inf2Rec_rate]))
    Inf2Inf = Inf - Inf2Rec
    Sus = Sus2Sus
    Inf = Inf2Inf + Sus2Inf
    Rec += Inf2Rec
    Track_s.append(Sus)
    Track_i.append(Inf)
    Track_r.append(Rec)


x = np.array([0, recursion_time])
plt.figure (figsize = (6,4), dpi = 150)
plt.plot(Track_i, label = "infected")
plt.plot(Track_r, label = "recovered")
plt.plot(Track_s, label = "supectible")
plt.xlabel("Time")
plt.ylabel("Number of people")
plt.title("SIR model")
plt.legend()
#plt.savefig("/user/Documents/Github/IBI1_2024-25/Practical6/SIR model", type = "png")
plt.show()