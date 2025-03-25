import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rdm
def vaccination(rate):

    Pop = int(10000 * (1-rate))
    if Pop > 0:
        Inf = 1 # can be changed into an input 
    else:
        Inf =0
         # Infecrd people
    Sus = Pop- Inf # Suspectible people
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
    if Pop == 0:
        for i in range(recursion_time):
            Track_i.append(0)
        return(Track_i)
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
    return(Track_i)

   
plt.figure (figsize = (6,4), dpi = 150)
for i in range(0, 11):
    rate = i/10
    Track_i = vaccination(rate)
    plt.plot(Track_i, label = f"{i*10}%")
plt.xlabel("Time")
plt.ylabel("Number of people")
plt.title("SIR model with different vaccination rates")
plt.legend()
#plt.savefig("/user/Documents/Github/IBI1_2024-25/Practical6/SIR model", type = "png")
plt.show()