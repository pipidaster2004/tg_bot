import json
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

def recreate_database()->None:
    with sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH")) as connection:
        connection.execute("DROP TABLE IF EXISTS telegram_updates")
        connection.execute("DROP TABLE IF EXISTS users")
        connection.execute("""CREATE TABLE IF NOT EXISTS telegram_updates
                           (
                                id INTEGER PRIMARY KEY,
                                payload TEXT NOT NULL
                           )"""
                           )
        connection.execute("""CREATE TABLE IF NOT EXISTS users
                           (
                                id INTEGER PRIMARY KEY,
                                telegram_id INTEGER NOT NULL UNIQUE,
                                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                state TEXT DEFAULT NULL,
                                order_json TEXT DEFAULT NULL
                           )"""
                           )
        
def persist_update(update: dict)->None:
    json_data = json.dumps(update, ensure_ascii=False, indent=2)
    with sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH")) as connection:
        connection.execute("INSERT INTO telegram_updates (payload) VALUES (?)", (json_data,)) 
    print(f"add {json_data} to table")

def ensure_user_exists(telegram_id: int) -> None:
    with sqlite3.connect(os.getenv("SQLITE_DATABASE_PATH")) as connection:
        cursor = connection.execute(
            "SELECT 1 FROM users WHERE telegram_id = ?", (telegram_id,)
        )

        if cursor.fetchone() is None:
            connection.execute(
                "INSERT INTO users (telegram_id) VALUES (?)", (telegram_id,)
            )
            print(f"add user_{telegram_id} to table")