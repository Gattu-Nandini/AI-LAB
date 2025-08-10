from numpy import asarray, exp
from numpy.random import randn, rand, seed
from matplotlib import pyplot as plt

# Objective function
def objective(x):
    return x[0]**2.0

# Simulated annealing algorithm
def simulated_annealing(objective, bounds, n_iterations, step_size, temp):
    # Generate an initial point
    best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    # Evaluate the initial point
    best_eval = objective(best)
    # Current working solution
    curr, curr_eval = best, best_eval
    scores = []

    # Run the algorithm
    for i in range(n_iterations):
        # Take a step
        candidate = curr + randn(len(bounds)) * step_size
        # Evaluate candidate point
        candidate_eval = objective(candidate)
        # Check for new best solution
        if candidate_eval < best_eval:
            best, best_eval = candidate, candidate_eval
        # Keep track of scores
        scores.append(best_eval)
        # Report progress
        print('>%d f(%s) = %.5f' % (i, best, best_eval))
        # Difference between candidate and current point evaluation
        diff = candidate_eval - curr_eval
        # Calculate temperature for current epoch
        t = temp / float(i + 1)
        # Calculate Metropolis acceptance criterion
        metropolis = exp(-diff / t)
        # Check if we should keep the new point
        if diff < 0 or rand() < metropolis:
            curr, curr_eval = candidate, candidate_eval

    return [best, best_eval, scores]

# Seed the pseudorandom number generator
seed(1)

# Define range for input
bounds = asarray([[-5.0, 5.0]])

# Define the total iterations
n_iterations = 1000

# Define the maximum step size
step_size = 0.1

# Initial temperature
temp = 10

# Perform the simulated annealing search
best, score, scores = simulated_annealing(objective, bounds, n_iterations, step_size, temp)
print('Done!')
print('f(%s) = %f' % (best, score))

# Line plot of best scores
plt.plot(scores, '.-')
plt.xlabel('Improvement Number')
plt.ylabel('Evaluation f(x)')
plt.title('Simulated Annealing Optimization Progress')
plt.grid(True)
plt.show()
