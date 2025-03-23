import matplotlib.pyplot as plt

colors = ["#607d8B", "#78909C", "#90A4AE", "#B0BEC5", "#CFD8DC"]

# Create a figure
plt.figure(figsize=(8, 2))

# Plot each color as a separate rectangle
for i, color in enumerate(colors):
    plt.fill_between([i, i + 1], 0, 1, color=color)

# Remove axis ticks and labels for clarity
plt.xlim(0, len(colors))
plt.axis('off')

# Display the plot
plt.show()
