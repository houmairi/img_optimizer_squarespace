import os
from PIL import Image
import argparse

def optimize_image(input_path, output_path, quality=85):
    with Image.open(input_path) as img:
        # Determine the output format
        if img.format == 'PNG' and img.mode == 'RGBA':
            # If it's a PNG with transparency, keep it as PNG
            img.save(output_path, 'PNG', optimize=True)
        else:
            # For other images, convert to JPG
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(output_path, 'JPEG', quality=quality, optimize=True)

def process_images(input_folder, output_folder, quality=85):
    input_folder = os.path.abspath(input_folder)
    output_folder = os.path.abspath(output_folder)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return

    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(root, input_folder)
                output_subdir = os.path.join(output_folder, relative_path)
                
                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)

                output_filename = os.path.splitext(filename)[0] + '.jpg'
                output_path = os.path.join(output_subdir, output_filename)

                try:
                    optimize_image(input_path, output_path, quality)
                    print(f"Optimized {filename} to {output_filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize images for Squarespace")
    parser.add_argument("input_folder", help="Path to the folder containing images")
    parser.add_argument("output_folder", help="Path to the folder where optimized images will be saved")
    parser.add_argument("-q", "--quality", type=int, default=85, help="Quality of JPG images (0-100, default: 85)")
    
    args = parser.parse_args()
    
    process_images(args.input_folder, args.output_folder, args.quality)