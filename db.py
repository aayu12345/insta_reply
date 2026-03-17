import sqlite3

# Connect to SQLite DB (creates file automatically)
conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS comments (
    comment_id TEXT PRIMARY KEY
)
""")
conn.commit()


# Check if comment already processed
def already_processed(comment_id):
    cursor.execute("SELECT 1 FROM comments WHERE comment_id=?", (comment_id,))
    return cursor.fetchone() is not None


# Save processed comment
def save_comment(comment_id):
    cursor.execute("INSERT OR IGNORE INTO comments (comment_id) VALUES (?)", (comment_id,))
    conn.commit()