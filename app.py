from flask import Flask, request, jsonify
from worker import process_comment

app = Flask(__name__)


@app.route("/webhook", methods=["GET"])
def verify():
    VERIFY_TOKEN = "my_verify_token"

    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")

    return "Verification failed"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    try:
        for entry in data.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})
                
                # Check if it's an Instagram comment webhook
                if change.get("field") == "comments" and "id" in value:
                    comment = {
                        "id": value["id"],
                        "text": value.get("text", "")
                    }
                    print("Received comment via webhook:", comment["text"])
                    process_comment(comment)

    except Exception as e:
        print("Webhook error:", e)

    return jsonify({"status": "ok"})


@app.route("/")
def dashboard():
    return "🚀 Instagram Automation Running (SQLite)"


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)