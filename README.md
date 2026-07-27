# Bangladeshi Note Detection Using Transfer Learning

An image classifier that identifies Bangladeshi Taka banknote denominations from photographs,
built to help visually impaired users identify currency independently. Four pretrained CNN
architectures are fine-tuned via transfer learning and compared, and a separate notebook
visualizes what the network actually "sees" at each convolutional layer.

## Dataset

A custom-collected set of photographs of Bangladeshi Taka banknotes, organized into one
subfolder per denomination (e.g. `ten/`, `fifty/`, `hundred/`, `twohundred/`, ...). The raw
dataset is not included in this repository — set it up as a sibling directory:

```
some-parent-folder/
├── BangladeshiNoteDetection-Using-Transfer-Learning/   (this repo)
└── data/
    └── note_dataset/
        ├── ten/
        ├── fifty/
        ├── hundred/
        └── ...
```

`resize.py` normalizes raw photos to a consistent 256x117 size before training:
```
python resize.py <denomination_folder_name>
```

Each notebook then splits the dataset 70% train / 20% validation / 10% test using
[`split-folders`](https://pypi.org/project/split-folders/).

## Notebooks

| Notebook | Architecture | Purpose |
|---|---|---|
| `DenseNet.ipynb` | DenseNet121 (last 6 layers fine-tuned) | Classification |
| `Resnet.ipynb` | ResNet50 (frozen backbone) | Classification |
| `KFold.ipynb` | ResNet50 with 5-fold cross-validation | Classification, more robust evaluation |
| `VGG.ipynb` | VGG16 (frozen backbone) | Classification |
| `FeatureMap.ipynb` | ResNet18 | Visualizes intermediate convolutional feature maps for a sample note, for interpretability rather than classification |

## Results

Test-set accuracy from the original training runs:

| Model | Test Accuracy | Classes |
|---|---|---|
| DenseNet121 | 98.80% | 9 |
| VGG16 | 97.67% | 9 |
| ResNet50 (5-fold CV) | 94.89% | 8 |
| ResNet50 (single split) | 89.11% | 9 |

DenseNet121 was the strongest performer. Note the ResNet50+K-Fold run used 8 classes while the
other three used 9 — kept as-is rather than silently changed, since it reflects what was actually
run; if you're comparing these numbers directly, be aware the label sets differ slightly.

## Tech Stack

- Python, PyTorch, torchvision
- split-folders (dataset splitting)
- Pillow (image preprocessing)
- matplotlib (training curves, feature map visualization)

## How to Run

1. Set up `data/note_dataset/<denomination>/` as a sibling directory (see [Dataset](#dataset)).
2. Install dependencies:
   ```
   pip install torch torchvision split-folders pillow matplotlib tqdm scikit-learn
   ```
3. Open any notebook in Jupyter and run all cells top to bottom.

## Contributors

- Mohibur Nabil
- Tateyama Orpa
