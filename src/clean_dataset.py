import os
import shutil
from PIL import Image
from tqdm import tqdm

# Input folders
real_input = r"C:\deepfake-image-detection\dataset\raw\real"
fake_input = r"C:\deepfake-image-detection\dataset\raw\fake"

# Output folders
real_output = r"C:\deepfake-image-detection\dataset\cleaned\real"
fake_output = r"C:\deepfake-image-detection\dataset\cleaned\fake"

# Create output folders if not present
os.makedirs(real_output, exist_ok=True)
os.makedirs(fake_output, exist_ok=True)

valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')


def clean_images(input_folder, output_folder):
    removed_count = 0
    kept_count = 0

    for filename in tqdm(os.listdir(input_folder)):
        file_path = os.path.join(input_folder, filename)

        try:
            # Skip non-image files
            if not filename.lower().endswith(valid_extensions):
                removed_count += 1
                continue

            # Open image and verify it
            img = Image.open(file_path)
            img.verify()

            # Reopen image after verify
            img = Image.open(file_path)

            # Remove very small images
            width, height = img.size
            if width < 64 or height < 64:
                removed_count += 1
                continue

            # Copy valid image to cleaned folder
            output_path = os.path.join(output_folder, filename)
            shutil.copy2(file_path, output_path)
            kept_count += 1

        except Exception:
            removed_count += 1

    print(f"\nFinished: {input_folder}")
    print(f"Kept: {kept_count}")
    print(f"Removed: {removed_count}")


clean_images(real_input, real_output)
clean_images(fake_input, fake_output)