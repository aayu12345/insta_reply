from services.instagram import reply_to_comment
from db import already_processed, save_comment

KEYWORD = "dm"
REPLY_TEXT = "Yes I am sending you, have you followed me?"


def process_comment(comment):
    comment_id = comment["id"]
    text = comment["text"]

    # Skip if already processed
    if already_processed(comment_id):
        return

    if KEYWORD in text.lower():
        print("Replying to:", text)

        response = reply_to_comment(comment_id, REPLY_TEXT)
        print("Response:", response)

        # Save to DB
        save_comment(comment_id)