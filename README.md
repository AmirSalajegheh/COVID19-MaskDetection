# 🚨 Mask Detection with YOLOv9

This project is a **real-time mask detection system** powered by **YOLOv9**. It detects people wearing masks or not in live webcam streams or pre-recorded videos and marks them with colored bounding boxes.

* Green box: person wearing a mask (safe)
* Red box: person without a mask (unsafe)

This system is ideal for monitoring mask compliance in offices, schools, and public areas.

---

## 📂 Project Structure

```
mask-detection/
│   main.py            
│   README.md          
│   requirements.txt   
│   training.ipynb     
│
└───Data
        model.pt       
        output.mp4     
```

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/AmirSalajegheh/COVID19-MaskDetection.git
cd mask-detection
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure **PyTorch** is installed with CUDA support if using a GPU.

---

## 🚀 Usage

### Run Detection:

```bash
python main.py
```

> The output video will be saved in `Data/output.mp4`.

### Train the Model:

Open `training.ipynb` in Jupyter Notebook or Google Colab and follow the instructions to train your YOLOv9 model.

---

## 🛠️ Tech Stack

* [PyTorch](https://pytorch.org/)
* [Ultralytics YOLOv9](https://github.com/ultralytics/ultralytics)
* [OpenCV](https://opencv.org/)

---

## 👨‍💻 Author

Developed by **Amir Salajegheh** 🚀
