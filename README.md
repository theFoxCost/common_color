# 🎯 Image Color Processor

This script processes an image, extracts three specific pixel colors, converts them from RGB to Hex format, and saves the result into a JSON file — all with precise execution timing.

---

## 🚀 Features

- ✅ Extracts colors from **3 key pixels**: top-left, bottom-right, and center.  
- ✅ Converts **RGB to Hex** using the `webcolors` library.  
- ✅ Saves color data to **color.json**.  
- ✅ Tracks processing time with **high precision** (`time.perf_counter()`).

---

## 🔧 Requirements

- Python 3.12+  
- Pillow (`PIL`) library  
- Webcolors library  

Install the dependencies:  

```bash
pip install pillow webcolors
```

---

## 🛠️ Usage

1️⃣ Run the script:  
```bash
python script_name.py
```

2️⃣ Enter the image file name (e.g., `image.jpg`).  

3️⃣ If the script can't find the image, input the correct directory.  

4️⃣ Check the generated `color.json` file for your colors!  

---

## 📁 Output Example

The script saves a file `color.json` like this:  

```json
{
  "common_color": "#d5a43a, #8c52ff, #1e90ff"
}
```

✅ Each color represents one of the 3 extracted pixels.  

---

## ⏱️ Time Tracking

After processing, it shows the time taken:  
```bash
Time taken: 0.34 seconds
```

---

## 🔥 Future Improvements

- 🎯 Detect **dominant** image colors  
- 🎯 Support **batch** image processing  
- 🎯 Add a **progress bar** for large images  

---

### 🌟 Author

Made by **theFoxCost** 🦊✨  

---

Happy coding! 🚀✨
