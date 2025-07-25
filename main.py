import time

def upload_to_youtube():
    print("✅ Uploaded to YouTube Shorts")

def upload_to_instagram():
    print("✅ Uploaded to Instagram Reels")

def upload_loop():
    video_path = "my_reel.mp4"
    caption = "🔥 Auto-reel! #reels #shorts"
    delay_minutes = 120

    for i in range(5):
        print(f"\n🔁 Upload #{i+1}")
        upload_to_youtube()
        upload_to_instagram()
        if i < 4:
            print(f"⏳ Waiting {delay_minutes} minutes...")
            time.sleep(delay_minutes * 60)

upload_loop()
