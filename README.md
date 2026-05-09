# 📚 LegacyLibrary
## Give old tablets a second life as distraction-free ebook readers.

A lightweight, Flask-powered ebook server specifically designed for legacy devices, such as the **iPad Mini 1**. 

LegacyLibrary provides a simple way to host, manage, and download your personal EPUB and PDF collection via a local network, featuring a lightweight early-2010s inspired interface.

## 🛠 The Workflow: Bridges the Gap

LegacyLibrary acts as a central hub for your digital library, allowing you to bypass the lack of modern cloud app support (like Google Drive or Dropbox) on older hardware:

1.  **Host:** Run the server on your main computer.
2.  **Upload:** Access the web interface from a **modern device** (PC, Mac, or Smartphone) to upload your `.epub` or `.pdf` files.
3.  **Sync:** The server automatically processes metadata and prepares the files.
4.  **Enjoy:** Open the site on your **legacy device**, download the books, and read them offline!

## ✨ Features

- **Optimized for Legacy Browsers:** Clean HTML/CSS using floats and standard JS that renders perfectly on older versions of Safari.
- **Automated Metadata Extraction:** Automatically extracts book covers from EPUB files using Python's `EbookLib` and `Pillow`.
- **Easy Management**
  - Custom styled upload buttons
  - Inline title editing
  - Quick download workflow
- **Privacy First:** Built to be hosted locally; your library stays on your private network.

## 🚀 Quick Start

### Prerequisites

- Python 3.x
- `pip` (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/lauar-m/LegacyLibrary.git](https://github.com/lauar-m/LegacyLibrary.git)
   cd LegacyLibrary

2. **Set up a Virtual Environment:**
   ```bash
    python -m venv venv
  
Activate it:

**On Windows:**
  ```bash
    venv\Scripts\activate
  ```
**On macOS/Linux:**
   ```bash
      source venv/bin/activate
   ```
3. **Install dependencies inside the venv:**
    ```bash
     pip install Flask EbookLib Pillow
    ```
4. **Run the server:**
   To make it accessible to your iPad over Wi-Fi, run:
     ```bash
     python app.py
     ```
Note: Ensure your computer and iPad are on the same Wi-Fi network. Access the server using http://<your-computer-ip>:5000.

### 📂 Usage Guide
#### On your Modern Device (Upload)
1. Navigate to the server IP.
2. Click "Choose File" and select your books.
3. Click "Upload to Shelf". The book is now hosted on your local "cloud".
   
#### On your Legacy Device (Download)
1. Open Safari on your legacy iPad or similar app.
2. Navigate to your server's IP address.
3. Click the **Download** button.
4. When the file opens, select **Open in iBooks** to save it permanently.
5. **Pro Tip:** Use the "Add to Home Screen" option in Safari to use LegacyLibrary as a standalone app!

### 🗺 Roadmap
- [x] EPUB upload and download
- [x] Automatic EPUB cover extraction
- [ ] EPUB metadata extraction
- [ ] Dark mode
- [ ] OPDS support


### Contributing
This project was born out of the need to give new life to old hardware. If you have ideas for improving performance on legacy browsers or adding new features, feel free to open an issue or submit a pull request.


*Developed with ❤️ by [Malu Lauar](https://github.com/lauar-m) to keep the joy of reading alive on every device.*
