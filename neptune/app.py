import neptune

# Create a Neptune run object
run = neptune.init_run(
    project="your-workspace-name/your-project-name", 
    api_token="YourNeptuneApiToken", 
    name="lotus-alligator", 
    tags=["quickstart", "script"],  # optional
)

# Log a single value
# Specify a field name ("seed") inside the run and assign a value to it
run["seed"] = 0.42

# Log a series of values
from random import random

epochs = 10
offset = random() / 5

for epoch in range(epochs):
    acc = 1 - 2**-epoch - random() / (epoch + 1) - offset
    loss = 2**-epoch + random() / (epoch + 1) + offset

    run["accuracy"].append(acc)
    run["loss"].append(loss)

# Upload an image
run["single_image"].upload("Lenna_test_image.png")

# Download the MNIST dataset
import mnist

train_images = mnist.train_images()
train_labels = mnist.train_labels()

# Upload a series of images
from neptune.types import File

for i in range(10):
    run["image_series"].append(
        File.as_image(
            train_images[i]
        ),  # You can upload arrays as images using the File.as_image() method
        name=f"{train_labels[i]}",
    )

# Stop the connection and synchronize the data with the Neptune servers
run.stop()