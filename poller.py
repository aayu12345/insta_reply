import time
from services.instagram import get_media
from worker import process_comment

def start_polling():
    print("🚀 Polling started...")

    while True:
        data = get_media()

        for media in data.get("data", []):
            comments = media.get("comments", {}).get("data", [])

            for comment in comments:
                process_comment(comment)

        time.sleep(30)


if __name__ == "__main__":
    start_polling()