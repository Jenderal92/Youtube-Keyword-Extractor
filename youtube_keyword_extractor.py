import os
import json
import requests

def print_banner():
    banner = """
    =============================================
       YOUTUBE KEYWORD EXTRACTOR
       Created By : Python 2.7
    =============================================
    """
    print(banner)

def get_keywords(api_key, video_id):
    base_url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "id": video_id,
        "key": api_key,
        "part": "snippet"
    }
    
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if "items" in data and len(data["items"]) > 0:
                try:
                    tags = data["items"][0]["snippet"]["tags"]
                    return tags
                except KeyError:
                    return "Video has no keywords."
            else:
                return "Video ID not found or invalid."
        else:
            return "Failed to retrieve data. Check the API Key or video ID."
    except Exception as e:
        return "Terjadi kesalahan: %s" % str(e)

def main():
    print_banner()
    
    api_key = "ur apikey here"
    video_id = raw_input("Enter YouTube Video ID: ").strip()
    
    print("\nGet keywords...\n")
    result = get_keywords(api_key, video_id)
    
    if isinstance(result, list):
        print("Keywords found:")
        for i, tag in enumerate(result, 1):
            print("%d. %s" % (i, tag))
    else:
        print(result)

    print("\nThank you for using YouTube Keyword Extractor!")

if __name__ == "__main__":
    main()
