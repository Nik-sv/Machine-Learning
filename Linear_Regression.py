import numpy as np
import matplotlib.pyplot as plt

# Generating sample data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Hyperparameters
learning_rate = 0.1
iterations = 1000

# Initializing parameters
m = np.random.randn(1)
c = np.random.randn(1)

# Gradient Descent Algorithm
for _ in range(iterations):
    y_pred = m * X + c  # Predictions
    error = y_pred - y  # Error Calculation

    # Compute Gradients
    dm = (2 / len(X)) * np.sum(error * X)
    dc = (2 / len(X)) * np.sum(error)

    # Update Parameters
    m -= learning_rate * dm
    c -= learning_rate * dc

# Plotting results
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, m * X + c, color="red", label="Predicted Line")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

print(f"Final m: {m}, Final c: {c}")
