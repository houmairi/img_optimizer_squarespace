# Squarespace Image Optimizer

This Python script optimizes images for use on Squarespace by converting and compressing them to formats supported by the platform.

## Features

- Processes PNG, JPG, JPEG, and GIF files
- Preserves PNG transparency where necessary
- Converts most images to optimized JPGs
- Maintains original folder structure in the output
- Allows customization of JPG compression quality

## Requirements

- Python 3.6 or higher
- Pillow library (specified in requirements.txt)

## Installation

1. Download or clone this repository:
   ```
   git clone https://github.com/houmairi/img_optimizer_squarespace.git
   ```
   Or download the ZIP file from the [repository page](https://github.com/houmairi/img_optimizer_squarespace) and extract it.

2. Navigate to the downloaded directory:
   ```
   cd img_optimizer_squarespace
   ```

3. Install the required dependencies using the requirements.txt file:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line:

```
python optimize_for_squarespace.py input_folder output_folder [-q QUALITY]
```

- `input_folder`: Path to the folder containing your original images
- `output_folder`: Path where optimized images will be saved
- `-q QUALITY`: Optional. JPG quality (0-100, default: 85)

Example:
```
python optimize_for_squarespace.py original optimized -q 90
```

## Notes

- This script converts static GIFs to JPGs. Animated GIFs require separate handling.
- Video files (MP4, MOV, M4V) are not processed by this script.
- Always review optimized images to ensure they meet your quality standards.

## License

[MIT License](https://opensource.org/licenses/MIT)