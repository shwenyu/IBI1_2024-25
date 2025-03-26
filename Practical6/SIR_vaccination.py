import numpy as np  # Import the numpy library for numerical operations
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import numpy.random as rdm  # Import numpy's random module for random number generation

def vaccination(rate):  # Define a function to simulate the SIR model with vaccination
    Pop = int(10000 * (1 - rate))  # Calculate the population after applying the vaccination rate
    if Pop > 0:  # Check if there are people left in the population
        Inf = 1  # Set the initial number of infected people
    else:  # If no population remains
        Inf = 0  # Set the number of infected people to 0
    Sus = Pop - Inf  # Calculate the initial number of susceptible people
    Rec = 0  # Initialize the number of recovered people
    beta = 0.3  # Basic infection rate, multiplied by the proportion of infected to calculate the infection rate
    gamma = 0.05  # Recovery rate
    Track_s = []  # List to store the number of susceptible people over time
    Track_s.append(Sus)  # Add the initial number of susceptible people to the list
    Track_i = []  # List to store the number of infected people over time
    Track_i.append(Inf)  # Add the initial number of infected people to the list
    Track_r = []  # List to store the number of recovered people over time
    Track_r.append(Rec)  # Add the initial number of recovered people to the list
    recursion_time = 1000  # Number of iterations (time steps)

    if Pop == 0:  # If no population remains after vaccination
        for i in range(recursion_time):  # Loop through each time step
            Track_i.append(0)  # Append 0 infected people for all time steps
        return(Track_i)  # Return the list of infected people

    for i in range(recursion_time):  # Loop through each time step
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
    return(Track_i)  # Return the list of infected people

plt.figure(figsize=(6, 4), dpi=150)  # Create a figure for the plot with specified size and resolution
for i in range(0, 11):  # Loop through vaccination rates from 0% to 100% in 10% increments
    rate = i / 10  # Calculate the vaccination rate
    Track_i = vaccination(rate)  # Simulate the SIR model with the given vaccination rate
    plt.plot(Track_i, label=f"{i * 10}%")  # Plot the infected count over time for the given vaccination rate
plt.xlabel("Time")  # Label the x-axis
plt.ylabel("Number of people")  # Label the y-axis
plt.title("SIR model with different vaccination rates")  # Add a title to the plot
plt.legend()  # Add a legend to the plot
# plt.savefig("/user/Documents/Github/IBI1_2024-25/Practical6/SIR model", type="png")  # Save the plot as a PNG file (commented out)
plt.show()  # Display the plot