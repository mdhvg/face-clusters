# Face Clusters

### Project structure

```
.
├── clean.py
├── embed.py
├── faces
│   ├── face1
│   └── face2
├── faces.py
├── flow.sh
├── imgs
│   ├── face1
│   └── face2
├── other-methods
│   ├── faces-mtcnn.py
│   ├── faces-nudenet.py
│   └── faces-retina.py
├── README.md
├── requirements.txt
└── viz.py
```

### Usage

- Clone the repo.
- Run `pip install -r requirements.txt`.
- Download the face dataset you like to use and set it according to the directory structure.
- Run the python files in this order (Or just run `flow.sh`):

```bash
python3 clean.py
python3 faces.py
python3 embed.py
```

## Conclusions

### Face Extraction

- MTCNN doesn't give much good results
- NudeNet is good but wastes compute on detecting other things
- retina-face is by far the best. Just uses a lot of resources. (Works good on Google Colab but, not recommended for local machine)

### Face recognition

- Facenet works just right
