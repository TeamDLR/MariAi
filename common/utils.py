import os
import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

def show_graphs(path_img1, path_img2, path_img3, path_img4, labels=None):
    '''
        Display the images in a 2x2 grid.
    '''
    
    # Check if the images files exist
    if not (os.path.exists(path_img1) and os.path.exists(path_img2)):
        print("Image files not found.")
        return

    if not (os.path.exists(path_img3) and os.path.exists(path_img4)):
        print("Image files not found.")
        return

    # Load and display images
    for i, path in enumerate([path_img1, path_img2]):
        img = plt.imread(path)
        plt.subplot(2, 2, i + 1)
        plt.imshow(img)
        plt.title(labels[i] if labels else "")
        plt.axis('off')

    # Show the images in a new window
    plt.tight_layout()

    # hide axis
    plt.axis('off')
    plt.show()
    


def save_graph(title, x_label, y_label, x_values, y_values, file_name):
    '''
    This function saves a graph as an image file.
    '''
    x = np.array(x_values)
    y = np.array(y_values)
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.axline((0, 0), slope=1, linestyle="--")
    plt.savefig(file_name)
    plt.show()


def concatenate_images_in_grid(folder_path, output_path, grid_cols=3):
    '''
    Given a folder path, reads all images in the folder and concatenates them into a grid.
    '''
    images = []

    # if output_path exists, delete it
    if os.path.exists(output_path):
        os.remove(output_path)

    # Load all images in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(folder_path, filename)
            img = cv2.imread(img_path)
            images.append(img)

    # Check if there are any images
    if not images:
        print("No images found in the specified folder.")
        return

    # Calculate the number of rows required in the grid
    grid_rows = math.ceil(len(images) / grid_cols)

    # Calculate the size of each cell in the grid
    cell_height = images[0].shape[0]
    cell_width = images[0].shape[1]

    # Resize all images to match the dimensions of each cell
    for i in range(len(images)):
        images[i] = cv2.resize(images[i], (cell_width, cell_height))

    # Create an empty grid
    grid = 255 * np.ones((grid_rows * cell_height, grid_cols * cell_width, 3), dtype=np.uint8)

    # Populate the grid with images
    for i, img in enumerate(images):
        row = i // grid_cols
        col = i % grid_cols
        grid[row * cell_height:(row + 1) * cell_height, col * cell_width:(col + 1) * cell_width] = img

    # Save the grid image
    cv2.imwrite(output_path, grid)
