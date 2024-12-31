# YouTube Keyword Extractor

![Youtube-Keyword-Extractor Jenderal92](https://github.com/user-attachments/assets/ff3d59ab-f7df-48b3-85b7-e3af76cdcc7b)


**YouTube Keyword Extractor** is a simple tool that allows users to extract keywords (tags) from a YouTube video using **YouTube Data API v3**. This tool is written in Python and is ideal for those looking to analyze video keywords for SEO, research, or content creation purposes.

---

## How to Use

### Prerequisites
- Python 2.7 installed on your computer.
- Active internet connection.
- A valid YouTube API Key. You can create an API Key by following [this guide](https://developers.google.com/youtube/registering_an_application).

### Steps
1. Clone this repository or download the file `youtube_keyword_extractor.py`.
2. Open your terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:
   ```
   python youtube_keyword_extractor.py
   ```
4. Enter YouTube API Key into source code 
5. Enter the Video ID of the YouTube video you want to extract keywords from.  
   Example Video ID: `dQw4w9WgXcQ` (from URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`).
6. The tool will display the extracted keywords.

---

## Features
- **Keyword Extraction:** Retrieve keywords from a YouTube video using the YouTube Data API.
- **Input Validation:** Ensures the Video ID entered are valid before sending requests.

---

## Example Output

### Input:

- **Video ID:** `dQw4w9WgXcQ`

### Output:
```
=============================================
   YOUTUBE KEYWORD EXTRACTOR
   Created By : Python 2.7
=============================================

Enter YouTube Video ID: dQw4w9WgXcQ

Get keywords...

Keywords found:
1. music
2. pop
3. 80s
4. rickroll

Thank you for using YouTube Keyword Extractor!
```

---

