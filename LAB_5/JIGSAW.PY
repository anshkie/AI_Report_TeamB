import numpy as np
import matplotlib.pyplot as plt
import random
import math

# 1. Load the scrambled image from a .mat file


def load_scrambled_image(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    dimensions = None
    image_data = []

    for line in lines:
        # Ignore comment lines
        if line.startswith('#'):
            continue
        # Read dimensions line
        if dimensions is None:
            dimensions = list(map(int, line.split()))
            continue

        # Read pixel values
        if line.strip():  # Ensure line is not empty
            image_data.append(list(map(int, line.split())))

    # Convert the list to a numpy array
    image_array = np.array(image_data, dtype=np.uint8)

    # Ensure the image dimensions match the expected height and width
    if dimensions is not None and len(dimensions) == 2:
        height, width = dimensions
        print(f"Expected dimensions: {height}x{width}, Loaded dimensions: {image_array.shape[0]}x{image_array.shape[1]}")
        if image_array.shape[0] != height or image_array.shape[1] != width:
            raise ValueError("Loaded image dimensions do not match specified dimensions.")

    return image_array

# 2. Function to split the image into puzzle pieces
def split_image(image, rows, cols):
    """Split the image into pieces."""
    height, width = image.shape
    piece_height = height // rows
    piece_width = width // cols
    pieces = []
    
    for r in range(rows):
        for c in range(cols):
            piece = image[r*piece_height:(r+1)*piece_height, c*piece_width:(c+1)*piece_width]
            pieces.append(piece)
    
    return pieces

# 3. Cost function to evaluate the arrangement
def cost_function(state, goal_state):
    mismatches = 0
    for s_piece, g_piece in zip(state, goal_state):
        if not np.array_equal(s_piece, g_piece):
            mismatches += 1
    return mismatches

# 4. Generate a neighboring state by swapping two pieces
def generate_neighbor(state):
    new_state = state.copy()
    idx1, idx2 = random.sample(range(len(state)), 2)
    # Swap two pieces
    new_state[idx1], new_state[idx2] = new_state[idx2], new_state[idx1]
    return new_state

# 5. Simulated annealing algorithm
def simulated_annealing(initial_state, goal_state, initial_temp=100, cooling_rate=0.99):
    current_state = initial_state
    current_cost = cost_function(current_state, goal_state)
    temperature = initial_temp

    while temperature > 1:
        neighbor = generate_neighbor(current_state)
        neighbor_cost = cost_function(neighbor, goal_state)
        delta_cost = neighbor_cost - current_cost

        if delta_cost < 0 or random.uniform(0, 1) < math.exp(-delta_cost / temperature):
            current_state = neighbor
            current_cost = neighbor_cost

        temperature *= cooling_rate

    return current_state

# 6. Reconstruct the image from pieces
def reconstruct_image(pieces, rows, cols):
    piece_height = pieces[0].shape[0]
    piece_width = pieces[0].shape[1]
    reconstructed_image = np.zeros((rows * piece_height, cols * piece_width), dtype=np.uint8)

    for r in range(rows):
        for c in range(cols):
            index = r * cols + c
            reconstructed_image[r*piece_height:(r+1)*piece_height, c*piece_width:(c+1)*piece_width] = pieces[index]
    
    return reconstructed_image

# 7. Display image
def display_image(image, title):
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.title(title)
    plt.show()

# Main flow
if __name__ == "__main__":
    # Path to the scrambled image file (.mat file)
    mat_file_path = 'scrambled_lena.mat'  # Change this to your actual path

    # Load the scrambled image
    scrambled_image = load_scrambled_image(mat_file_path)
    
    # Define the number of rows and columns (puzzle size)
    rows, cols = 8, 8  # Example: splitting into 8x8 grid, adjust as necessary

    # Split both scrambled and original image into pieces
    scrambled_pieces = split_image(scrambled_image, rows, cols)

    # Assuming you have the original (goal) image for comparison (load original Lena image)
    # Load or simulate original Lena image (goal image)
    # For this example, let's use the scrambled image pieces as the "goal" arrangement
    goal_state = scrambled_pieces.copy()  # For simplicity, the correct arrangement is the current one
    
    # Shuffle the scrambled pieces to simulate the puzzle
    initial_state = scrambled_pieces.copy()
    random.shuffle(initial_state)

    # Solve the puzzle using simulated annealing
    solution = simulated_annealing(initial_state, goal_state)

    # Reconstruct and display the solved image
    solved_image = reconstruct_image(solution, rows, cols)
    display_image(solved_image, "Solved Lena Image")
