# Particle Swarm Optimization (PSO) 3D For Global Optima/Minima

![Python](https://img.shields.io/badge/python-3.x-blue.svg)

## Description

This Python code implements the Particle Swarm Optimization (PSO) algorithm to find the global minimum or maximum of a given objective function. PSO is inspired by the collective behavior of particles in nature and aims to efficiently search for optimal solutions in a multidimensional space.

The PSO algorithm simulates a swarm of particles, where each particle represents a potential solution. It iteratively updates the position and velocity of the particles to converge towards the global minimum or maximum of the objective function. Additionally, the code provides 3D visualization to understand the search process and visualize the final optimal solution.

## Features

- Efficient Particle Swarm Optimization algorithm for global minimization and maximization
- Scalable and customizable for different objective functions
- Easily adaptable to various application domains
- Visualization of the optimization process in a 3D plot for better understanding and analysis

## Requirements

- Python 3.x
- NumPy
- Matplotlib (for visualization, optional)

## Getting Started

1. Clone the repository:
git clone https://github.com/BouchanaHicham/Particle-Swarm-Optimization-3D
cd particle_swarm_optimization


2. Install the required dependencies:
pip install numpy matplotlib


3. Customize the objective function in the `shape(x)` function to fit your specific optimization problem.

4. Set the initial position (`x0`) and bounds (`bounds`) for each dimension of the search space.

5. Run the PSO algorithm by executing the script.

6. The script will find the global minimum or maximum of the objective function, depending on the optimization mode selected by the user, and display the results in a 3D plot.

## Parameters

- `func`: The objective function to be minimized.
- `x0`: The initial position in the search space.
- `bounds`: The lower and upper bounds for each dimension of the search space.
- `num_particles`: Number of particles in the swarm (default: 20).
- `maxiter`: Maximum number of iterations for the algorithm (default: 100).
- `optimize_mode`: Choose 'min' for global minimization or 'max' for global maximization.

## Examples
### Sphere Function (Maximization)
```python
# Define the function to be minimized
def shape(x):
    #                               --- sphere ---
    scaling_factor = 5  # Adjust scaling factor to fit within 0 to 1000
    return scaling_factor * sum([xi ** 2 for xi in x])

# Run the particle swarm optimization algorithm with 20 particles for 100 iterations
best_position, best_fitness = particle_swarm_optimization(shape, x0, bounds, num_particles=20, maxiter=100, optimize_mode="max")
```

![Sphere Function](https://github.com/BouchanaHicham/Particle-Swarm-Optimization-3D/blob/main/Examples/Sphere/Sphere.png)<br>
Best position: [10, 10]<br>
Best fitness: 1000.0
### Ackley Function (Maximization)
```python
# Define the function to be minimized
def shape(x):
    #                               --- Ackley Function --- 
    scaling_factor = 40  # Adjust scaling factor to fit within 0 to 1000
    n = len(x)
    return scaling_factor * (-20 * np.exp(-0.2 * np.sqrt((1/n) * sum([xi ** 2 for xi in x]))) - np.exp((1/n) * sum([np.cos(2 * np.pi * xi) for xi in x])) + 20 + np.exp(1))

# Run the particle swarm optimization algorithm with 20 particles for 100 iterations
best_position, best_fitness = particle_swarm_optimization(shape, x0, bounds, num_particles=20, maxiter=100, optimize_mode="max")
```

![Ackley Function](https://github.com/BouchanaHicham/Particle-Swarm-Optimization-3D/blob/main/Examples/Ackley%20Function/Ackley%20Function.png)<br>
Best position: [0.5048011421391644, 9.597194159185335] <br>
Best fitness: 687.1121449350245
### Ackley Function (Minimization)
```python
# Define the function to be minimized
def shape(x):
    #                               --- Zakharov Function ---  
    return sum([x[i]**2 for i in range(len(x))]) + (0.5 * sum([i * x[i] for i in range(len(x))]))**2 + (0.5 * sum([i * x[i] for i in range(len(x))]))**4

# Run the particle swarm optimization algorithm with 20 particles for 100 iterations
best_position, best_fitness = particle_swarm_optimization(shape, x0, bounds, num_particles=20, maxiter=100, optimize_mode="min")  # Notice how we changed the 'optimize_mode' to "min" 
```

![Zakharov Function](https://github.com/BouchanaHicham/Particle-Swarm-Optimization-3D/blob/main/Examples/Zakharov%20Function/Zakharov%20Function%20(min).png)<br>
Best position: [-1.6213931380268527e-11, -4.87704978117861e-12]<br>
Best fitness: -2.9262358901417433e-22

## License

This project is licensed under the MIT License. You can find the full text of the license in the [LICENSE](LICENSE) file.

## Contributions

Contributions to this project are more than welcome. If you have any suggestions, bug fixes, or new features to add, please feel free to fork the repository and submit a pull request. We value your feedback and contributions!

## Author

**Bouchana Hicham**
