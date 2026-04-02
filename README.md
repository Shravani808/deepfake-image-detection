# AI-Generated vs Real Image Detection Using Deep Learning

This project uses deep learning and transfer learning techniques to classify whether a face image is **real** or **AI-generated (deepfake)**.

---

## Project Structure

```
deepfake-image-detection/
├── dataset/
│   ├── cleaned/          # Images after cleaning (excluded from Git)
│   ├── train/            # Training split (excluded from Git)
│   ├── val/              # Validation split (excluded from Git)
│   └── test/             # Test split (excluded from Git)
├── models/               # Saved trained models
├── notebooks/            # Jupyter notebooks for experiments
├── outputs/              # Training outputs, plots, logs
├── src/
│   ├── clean_dataset.py  # Remove corrupted, invalid & tiny images
│   ├── remove_duplicates.py  # Perceptual hash-based duplicate removal
│   └── split_dataset.py  # Train/Val/Test split (70/15/15)
├── dataset_info.md       # Detailed dataset statistics
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Dataset

| Stage | Real Images | Fake Images | Total |
|---|--:|--:|--:|
| Raw | 70,000 | 70,000 | 140,000 |
| After Cleaning | 70,000 | 70,000 | 140,000 |
| After Duplicate Removal | 69,709 | 64,682 | 134,391 |

- **Cleaning** removes corrupted files, non-image files, and images smaller than 64×64 px.
- **Duplicate removal** uses perceptual hashing (`imagehash`) to detect and remove near-duplicate images.
- **Split ratio** — Train: 70% · Validation: 15% · Test: 15% (seed `42` for reproducibility).

> The dataset focuses exclusively on **face images** and is excluded from version control via `.gitignore`.

---

## Data Preprocessing Pipeline

Run the scripts in order from the `src/` directory:

```bash
# Step 1 — Clean raw images
python src/clean_dataset.py

# Step 2 — Remove duplicate images
python src/remove_duplicates.py

# Step 3 — Split into train / val / test
python src/split_dataset.py
```

---

## Technologies Used

- **Python**
- **TensorFlow / Keras** — Model training & transfer learning
- **OpenCV** — Image processing
- **Pillow** — Image validation & loading
- **imagehash** — Perceptual hashing for duplicate detection
- **NumPy / Pandas** — Data manipulation
- **Matplotlib** — Visualization
- **Scikit-learn** — Evaluation metrics
- **tqdm** — Progress bars

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/Shravani808/deepfake-image-detection.git
cd deepfake-image-detection

# Install dependencies
pip install -r requirements.txt
```

---

## Current Progress

- [x] Dataset collected (70k real + 70k fake face images)
- [x] Dataset cleaned (corrupted / invalid / tiny images removed)
- [x] Duplicate images removed via perceptual hashing
- [x] Train / Validation / Test split created
- [ ] Model training with transfer learning
- [ ] Model evaluation & results

---

## License

This project is licensed under the [MIT License](LICENSE).
