import sqlite3
import json
import os

class MemoryEngine:
    def __init__(self, db_path='database/memory.db', personality_config='config/personality.yaml'):
        self.db_path = db_path
        self.personality_config = personality_config
        self.connection = self.create_connection()
        self.load_personality()

    def create_connection(self):
        conn = sqlite3.connect(self.db_path)
        self.create_memory_table(conn)
        return conn

    def create_memory_table(self, conn):
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_input TEXT,
                ai_response TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

    def remember(self, user_input, ai_response):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO memory (user_input, ai_response) VALUES (?, ?)
        ''', (user_input, ai_response))
        self.connection.commit()

    def recall(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT user_input, ai_response, timestamp FROM memory ORDER BY timestamp DESC')
        return cursor.fetchall()

    def clear_memory(self):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM memory')
        self.connection.commit()

    def load_personality(self):
        if os.path.exists(self.personality_config):
            with open(self.personality_config, 'r') as file:
                self.personality = json.load(file)
        else:
            self.personality = {}

    def get_personality_trait(self, trait):
        return self.personality.get(trait, "Trait not found.")

    def close(self):
        self.connection.close()