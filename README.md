# Food Platform Image Optimizer 🍔📸

A lightweight Python desktop application designed to help restaurant owners and developers quickly format product photos for food delivery platforms (such as Yemeksepeti, Getir, or Trendyol Yemek). 

## The Problem
Many food delivery platforms have strict image requirements:
*   **Minimum Resolution:** e.g., 1000px x 731px
*   **File Size Range:** e.g., Must be between 200KB and 500KB.
*   **Format:** Usually restricted to JPEG/JPG.

Manual editing can be time-consuming when dealing with hundreds of menu items. This tool automates the process to save time and ensure compliance.

## The Solution
This tool provides a **Drag & Drop** interface that automatically:
1.  Scales the image to a safe resolution (2000px width) to pass resolution checks.
2.  Adjusts JPEG quality and subsampling to ensure the file size stays above the 200KB threshold without losing visual clarity.
3.  Converts various formats (.png, .webp, .jpeg) into standardized .jpg files.
4.  Organizes processed images into a dedicated folder on the Desktop for easy access.

## Tech Stack
*   **Language:** Python 3.x
*   **GUI:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Modern UI)
*   **Image Processing:** [Pillow (PIL)](https://python-pillow.org/)
*   **Functionality:** [TkinterDnD2](https://github.com/pmgagne/tkinterdnd2) for drag-and-drop support.

## Installation

```bash
# 1. Clone the repository
git clone [https://github.com/your-username/food-image-optimizer.git](https://github.com/your-username/food-image-optimizer.git)

# 2. Install the required dependencies
pip install customtkinter Pillow tkinterdnd2

# 3. Run the application
python YemeksepetiFixer.py
```
## Usage
🚀 Launch: Run the script to open the modern dark-themed window.

🖱️ Drag & Drop: Simply select your product images from your folder and drop them onto the application area.

⚡ Automated Export: The tool will process the images instantly.

📂 Access: Your optimized images will be ready in the Yemeksepeti_Yukle folder on your Desktop.

## Developed by Sümeyra Koyuncu
