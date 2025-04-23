import numpy as np  # Import the numpy library for numerical operations
import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Initialize the population grid
pop = np.zeros((100, 100), dtype=int)  # Create a 100x100 grid initialized with zeros (susceptible state)
outbreak_x, outbreak_y = np.random.choice(100, 2)  # Randomly select the initial outbreak location
pop[outbreak_x, outbreak_y] = 1  # Set the initial outbreak location to infected state

# Initialize the simulation parameters
loop_time = 1000  # Set the number of simulation iterations
beta = 0.3  # Set the infection rate
gamma = 0.05  # Set the recovery rate
prop = 500  # Set the number of immune individuals

# Assign immune individuals randomly in the grid
immune_spots = []  # Initialize a list to store immune spots
for _ in range(prop):  # Loop to assign immune individuals
    while True:  # Repeat until a valid immune spot is found
        x, y = np.random.randint(0, 100), np.random.randint(0, 100)  # Randomly select a grid cell
        if (x, y) != (outbreak_x, outbreak_y) and pop[x, y] == 0:  # Ensure it is not the outbreak point or already occupied
            pop[x, y] = -1  # Mark the cell as immune
            immune_spots.append((x, y))  # Add the immune spot to the list
            break  # Exit the loop for this immune individual

# initialize the counts of susceptible, infected, and recovered individuals
Sus = 100 * 100 - prop - 1  # Calculate the initial number of susceptible individuals
Inf = 1  # Initialize the number of infected individuals
Rec = 0  # Initialize the number of recovered individuals

# define the directions for infection spread
directions = [(-1, -1), (-1, 0), (-1, 1),  # Define the 8 possible directions for infection spread
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

def spread_infection(x, y):
    global Inf, Sus, Rec  # Declare global variables to modify them
    # deal with recovery
    if pop[x, y] == 1:  # Check if the current cell is infected
        if np.random.rand() < gamma:  # Determine if the individual recovers based on the recovery rate
            pop[x, y] = 2  # Mark the cell as recovered
            Inf -= 1  # Decrease the infected count
            Rec += 1  # Increase the recovered count
        else:
            # deal with infection spread
            for dx, dy in directions:  # Iterate over all possible directions
                nx, ny = x + dx, y + dy  # Calculate the neighboring cell coordinates
                if 0 <= nx < 100 and 0 <= ny < 100:  # Ensure the neighbor is within bounds
                    if pop[nx, ny] == 0:  # Check if the neighbor is susceptible
                        # calculate the infection probability based on the number of infected neighbors
                        infected_neighbors = 0  # Initialize the count of infected neighbors
                        for ddx, ddy in directions:  # Iterate over all directions to count infected neighbors
                            nnx, nny = nx + ddx, ny + ddy  # Calculate the neighbor's neighbor coordinates
                            if 0 <= nnx < 100 and 0 <= nny < 100:  # Ensure the neighbor's neighbor is within bounds
                                if pop[nnx, nny] == 1:  # Check if the neighbor's neighbor is infected
                                    infected_neighbors += 1  # Increment the infected neighbor count
                        infection_prob = beta * (infected_neighbors / 8)  # Calculate the infection probability
                        if np.random.rand() < infection_prob:  # Determine if the neighbor gets infected
                            pop[nx, ny] = 1  # Mark the neighbor as infected
                            Inf += 1  # Increase the infected count
                            Sus -= 1  # Decrease the susceptible count

def draw():
    plt.clf()  # Clear the current figure
    plt.imshow(pop, cmap='viridis', interpolation='nearest')  # Display the grid with a color map
    plt.title(f"SIR Model: Sus={Sus}, Inf={Inf}, Rec={Rec}")  # Set the title with current counts
    plt.pause(0.1)  # Pause to update the plot

# Main simulation loop
plt.figure(figsize=(8, 6))  # Create a figure for the plot
for t in range(loop_time):  # Loop through the simulation iterations

    infected = np.argwhere(pop == 1)  # Find all currently infected cells
    for (x, y) in infected:  # Iterate over all infected cells
        spread_infection(x, y)  # Spread infection from each infected cell
    draw()  # Update the plot
plt.show()  # Display the final plot