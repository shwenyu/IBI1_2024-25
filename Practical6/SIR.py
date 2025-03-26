import numpy as np  # Import the numpy library for numerical operations
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import numpy.random as rdm  # Import numpy's random module for random number generation

Pop = 10000  # Total population, can be changed to an input
Inf = 1  # Initial number of infected people
Sus = Pop - 1  # Initial number of susceptible people (total population minus infected)
Rec = 0  # Initial number of recovered people

beta = 0.3  # Basic infection rate, multiplied by the proportion of infected to calculate the infection rate
gamma = 0.05  # Recovery rate

Track_s = []  # List to store the number of susceptible people over time
Track_s.append(Sus)  # Add the initial number of susceptible people to the list
Track_i = []  # List to store the number of infected people over time
Track_i.append(Inf)  # Add the initial number of infected people to the list
Track_r = []  # List to store the number of recovered people over time
Track_r.append(Rec)  # Add the initial number of recovered people to the list

recursion_time = 1000  # Number of iterations (time steps), can be changed

# Loop through each time step
for i in range(recursion_time):
    Sus2Inf_rate = beta * (Inf / Pop)  # Calculate the rate of susceptible people becoming infected
    Inf2Rec_rate = gamma  # Recovery rate remains constant
    Sus2Inf = sum(rdm.choice(range(2), Sus, p=[1 - Sus2Inf_rate, Sus2Inf_rate]))  # Simulate the number of new infections
    Sus2Sus = Sus - Sus2Inf  # Update the number of susceptible people
    Inf2Rec = sum(rdm.choice(range(2), Inf, p=[1 - Inf2Rec_rate, Inf2Rec_rate]))  # Simulate the number of recoveries
    Inf2Inf = Inf - Inf2Rec  # Update the number of infected people
    Sus = Sus2Sus  # Update the susceptible count
    Inf = Inf2Inf + Sus2Inf  # Update the infected count
    Rec += Inf2Rec  # Update the recovered count
    Track_s.append(Sus)  # Append the updated susceptible count to the list
    Track_i.append(Inf)  # Append the updated infected count to the list
    Track_r.append(Rec)  # Append the updated recovered count to the list

x = np.array([0, recursion_time])  # Create an array for the x-axis (time steps)

plt.figure(figsize=(6, 4), dpi=150)  # Create a figure for the plot with specified size and resolution
plt.plot(Track_i, label="infected")  # Plot the infected count over time
plt.plot(Track_r, label="recovered")  # Plot the recovered count over time
plt.plot(Track_s, label="susceptible")  # Plot the susceptible count over time
plt.xlabel("Time")  # Label the x-axis
plt.ylabel("Number of people")  # Label the y-axis
plt.title("SIR model")  # Add a title to the plot
plt.legend()  # Add a legend to the plot
# plt.savefig("/user/Documents/Github/IBI1_2024-25/Practical6/SIR model", type="png")  # Save the plot as a PNG file (commented out)
plt.show()  # Display the plot