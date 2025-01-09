from PIL import Image

# Open an image file
input_image = "harman.png"
output_image = "harman_resized.png"
desired_width = 240  # Desired width
desired_height = 240  # Desired height

# Open the image
image = Image.open(input_image)

# Resize the image
resized_image = image.resize((desired_width, desired_height))

# Save the resized image
resized_image.save(output_image)

print(f"Image resized to {desired_width}x{desired_height} and saved as {output_image}")
