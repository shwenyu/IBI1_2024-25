import numpy as np  # Import the numpy library for numerical operations
import matplotlib.pyplot as plt  # Import matplotlib for plotting

pop = np.zeros((100, 100))  # Initialize a 100x100 grid with all elements set to 0
outbreak = np.random.choice(range(100), 2)  # Randomly select a starting point for the outbreak
pop[outbreak[0], outbreak[1]] = 1  # Set the outbreak point as infected (state = 1)

loop_time = 100  # Define the number of iterations for the simulation
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
Inf = 0  # Initialize the count of infected individuals
Sus = 100 * 100  # Initialize the count of susceptible individuals
prop = 500  # Number of immune individuals to introduce

# for n in range(prop):  # Uncomment to introduce immune individuals
#     x = np.random.randint(0, 100)  # Randomly select x-coordinate
#     y = np.random.randint(0, 100)  # Randomly select y-coordinate
#     pop[x, y] = -1  # Set the cell as immune (state = -1)

def infect(x, y):  # Define the infection process for a given cell
    global Inf, Sus  # Use global variables for infected and susceptible counts
    draw()  # Update the visualization
    if (x < 0 or y < 0 or x >= 100 or y >= 100):  # Check if the cell is out of bounds
        return()  # Exit the function if out of bounds
    else:
        if pop[x, y] == 0:  # If the cell is susceptible
            count = 0  # Initialize the count of infected neighbors
            for i in (1, -1):  # Iterate over neighboring cells in x-direction
                for j in (1, -1):  # Iterate over neighboring cells in y-direction
                    if 0 <= x + i <= 99 and 0 <= y + j <= 99:  # Check if neighbor is within bounds
                        if pop[x + i, y + j] == 1:  # Check if neighbor is infected
                            count += 1  # Increment the count of infected neighbors
            Inf_rate = 0.25 * count  # Calculate the infection rate based on neighbors
            beta_new = beta * Inf_rate  # Adjust beta based on infection rate
            state = sum(np.random.choice(range(2), 1, p=[1 - Inf_rate, Inf_rate]))  # Determine if infection occurs
            pop[x, y] = state  # Update the cell state
        elif pop[x, y] == 1:  # If the cell is infected
            if np.random.random() <= gamma:  # Check if the cell recovers
                pop[x, y] = 2  # Update the cell state to recovered
            else:
                Inf += 1  # Increment the infected count
                Sus -= 1  # Decrement the susceptible count
                for i in (1, -1):  # Iterate over neighboring cells in x-direction
                    for j in (1, -1):  # Iterate over neighboring cells in y-direction
                        infect(x + i, y + j)  # Attempt to infect neighbors
        elif pop[x, y] == 2 or pop[x, y] == -1:  # If the cell is recovered or immune
            return()  # Exit the function

def draw():  # Define the function to visualize the grid
    plt.figure(figsize=(6, 4), dpi=150)  # Set the figure size and resolution
    plt.clf()  # Clear the current figure
    plt.imshow(pop, cmap='viridis', interpolation='nearest')  # Display the grid
    plt.title("Spatial SIR Model")  # Add a title to the plot
    plt.pause(1)  # Pause to update the visualization

# Main loop
infect(outbreak[0], outbreak[1])  # Start the infection process from the outbreak point
