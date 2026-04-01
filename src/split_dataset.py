import os
import shutil
import random

random.seed(42)

# Source folders
real_source = r"C:\deepfake-image-detection\dataset\final\real"
fake_source = r"C:\deepfake-image-detection\dataset\final\fake"

# Destination base folder
base_output = r"C:\deepfake-image-detection\dataset"


# Split ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15


def split_images(source_folder, class_name):
    images = os.listdir(source_folder)
    random.shuffle(images)

    total = len(images)
    train_end = int(total * train_ratio)
    val_end = train_end + int(total * val_ratio)

    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    for split_name, split_images_list in {
        'train': train_images,
        'val': val_images,
        'test': test_images
    }.items():

        output_folder = os.path.join(base_output, split_name, class_name)
        os.makedirs(output_folder, exist_ok=True)

        for image_name in split_images_list:
            src_path = os.path.join(source_folder, image_name)
            dst_path = os.path.join(output_folder, image_name)
            shutil.copy2(src_path, dst_path)

    print(f"\n{class_name.upper()} SPLIT COMPLETED")
    print(f"Total Images: {total}")
    print(f"Train: {len(train_images)}")
    print(f"Validation: {len(val_images)}")
    print(f"Test: {len(test_images)}")


split_images(real_source, 'real')
split_images(fake_source, 'fake')