from PIL import Image
import os

def convert_to_webp(input_image_path, output_image_path, lossy=True, max_size_ratio=0.8, quality=80):
    """
    Convert an image to WebP format with specified compression settings.

    Parameters:
        input_image_path (str): Path to the input image file.
        output_image_path (str): Path to save the output WebP image file.
        lossy (bool): Whether to use lossy compression (True) or lossless compression (False).
        max_size_ratio (float): Maximum allowed size ratio between the WebP image and the original image.
        quality (int): Quality level (0-100) for lossy compression. Ignored if lossy=False.
    """
    # Open the input image
    with Image.open(input_image_path) as img:
        original_size = os.path.getsize(input_image_path)
        
        # Convert to lossy WebP format with specified quality
        if lossy:
            img.save(output_image_path, 'WEBP', quality=quality)
        else:
            img.save(output_image_path, 'WEBP', lossless=True)
        
        # Check the size of the WebP image
        webp_size = os.path.getsize(output_image_path)
        
        # If the size of the WebP image exceeds the original size multiplied by the maximum allowed ratio,
        # apply additional compression until the size requirement is met
        while webp_size > original_size * max_size_ratio:
            if lossy:
                # Reduce quality by 10 units
                quality -= 10
                img.save(output_image_path, 'WEBP', quality=quality)
            else:
                # Use default settings for lossless compression
                img.save(output_image_path, 'WEBP', lossless=True)
            
            webp_size = os.path.getsize(output_image_path)
            if quality <= 0:
                break

# Example usage:
input_image_path = 'E:\\Semester-2\\python_codes\\DSC00975_lossy.webp'  # Replace with the path to your input image
output_path = 'E:\\Semester-2\\python_codes\\DSC00975_lossy1.webp'  # Output path for WebP image

# Convert to lossy WebP format with maximum size ratio of 70% compared to the original image
convert_to_webp(input_image_path, output_path, lossy=True, max_size_ratio=0.1, quality=70)
