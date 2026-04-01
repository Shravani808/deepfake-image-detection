import os
import shutil
from PIL import Image
import imagehash
from tqdm import tqdm

# Input folders
real_input = r"C:\deepfake-image-detection\dataset\cleaned\real"
fake_input = r"C:\deepfake-image-detection\dataset\cleaned\fake"

# Output folders
real_output = r"C:\deepfake-image-detection\dataset\final\real"
fake_output = r"C:\deepfake-image-detection\dataset\final\fake"

os.makedirs(real_output, exist_ok=True)
os.makedirs(fake_output, exist_ok=True)


def remove_duplicates(input_folder, output_folder):
    hashes = set()
    kept = 0
    removed = 0

    for filename in tqdm(os.listdir(input_folder)):
        file_path = os.path.join(input_folder, filename)

        try:
            img = Image.open(file_path)
            img_hash = imagehash.average_hash(img)

            if img_hash in hashes:
                removed += 1
                continue

            hashes.add(img_hash)
            shutil.copy2(file_path, os.path.join(output_folder, filename))
            kept += 1

        except Exception:
            removed += 1

    print(f"\nFinished: {input_folder}")
    print(f"Kept: {kept}")
    print(f"Removed duplicates: {removed}")


remove_duplicates(real_input, real_output)
remove_duplicates(fake_input, fake_output)