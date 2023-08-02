import random
import matplotlib.pyplot as plt
import numpy as np

class Particle:
    def __init__(self, x0):
        self.position = []   # particle position
        self.velocity = []   # particle velocity
        self.best_position = []  # best position individual particle has achieved
        self.best_fitness = -1  # best fitness individual particle has achieved
        
        for i in range(0, num_dimensions):
            self.velocity.append(random.uniform(-1, 1))
            self.position.append(x0[i])
        
    def evaluate(self, cost_func, optimize_mode):
        if optimize_mode == 'min':
            self.fitness = -cost_func(self.position)
        if optimize_mode == 'max':
            self.fitness = cost_func(self.position)
        
        if self.fitness > self.best_fitness or self.best_fitness == -1:
            self.best_position = self.position
            self.best_fitness = self.fitness
            
    def update_velocity(self, best_position_group):
        w = 0.5   # inertia weight
        c1 = 1    # cognitive weight
        c2 = 2    # social weight
        
        for i in range(0, num_dimensions):
            r1 = random.random()
            r2 = random.random()
            
            cognitive_velocity = c1 * r1 * (self.best_position[i] - self.position[i])
            social_velocity = c2 * r2 * (best_position_group[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + cognitive_velocity + social_velocity
            
            
    def update_position(self, bounds):
        for i in range(0, num_dimensions):
            self.position[i] = self.position[i] + self.velocity[i]
            
            # adjust maximum position if necessary
            if self.position[i] > bounds[i][1]:
                self.position[i] = bounds[i][1]
            
            # adjust minimum position if necessary
            if self.position[i] < bounds[i][0]:
                self.position[i] = bounds[i][0]
                

def particle_swarm_optimization(cost_func, x0, bounds, num_particles, maxiter, optimize_mode):
    global num_dimensions
    
    num_dimensions = len(x0)
    best_fitness_group = -1
    best_position_group = []
    swarm = []
    
    for i in range(0, num_particles):
        swarm.append(Particle(x0))
        
    for i in range(0, maxiter):
        for j in range(0, num_particles):
            swarm[j].evaluate(cost_func, optimize_mode)
            
            if swarm[j].fitness > best_fitness_group or best_fitness_group == -1:
                best_position_group = list(swarm[j].position)
                best_fitness_group = float(swarm[j].fitness)
                
        for j in range(0, num_particles):
            swarm[j].update_velocity(best_position_group)
            swarm[j].update_position(bounds)
            
    return best_position_group, best_fitness_group

# Define the cost function (in this case, the shape function)
def shape(x):
    
   
    #                               --- sphere ---
    #scaling_factor = 5  # Adjust scaling factor to fit within 0 to 1000
    #return scaling_factor * sum([xi ** 2 for xi in x])
    
    #                               --- Ackley Function --- 
    #scaling_factor = 40  # Adjust scaling factor to fit within 0 to 1000
    #n = len(x)
    #return scaling_factor * (-20 * np.exp(-0.2 * np.sqrt((1/n) * sum([xi ** 2 for xi in x]))) - np.exp((1/n) * sum([np.cos(2 * np.pi * xi) for xi in x])) + 20 + np.exp(1))
    
    #                               --- Zakharov Function ---  
    return sum([x[i]**2 for i in range(len(x))]) + (0.5 * sum([i * x[i] for i in range(len(x))]))**2 + (0.5 * sum([i * x[i] for i in range(len(x))]))**4


# Define the initial position and bounds for each dimension
x0 = [0.8, 1.2]
bounds = [(-10, 10), (-10, 10)]

# Run the particle swarm optimization algorithm with 20 particles for 100 iterations
best_position, best_fitness = particle_swarm_optimization(shape, x0, bounds, num_particles=20, maxiter=100, optimize_mode="min")

# Generate data for the shape function
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = shape([X, Y])

# Plot the shape function
# Plot the shape function
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)

# Add the particle swarm optimization solution to the plot
ax.scatter(best_position[0], best_position[1], best_fitness, color='red', s=100)

# Set the plot limits and labels
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(0, 1000)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

# Display the results
print("Best position:", best_position)
print("Best fitness:", best_fitness)