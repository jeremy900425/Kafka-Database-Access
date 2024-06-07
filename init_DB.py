import base64
import sqlite3

DATABASE = 'database.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            UserID TEXT PRIMARY KEY,
            UserName TEXT,
            Account TEXT,
            Password TEXT,
            Avatar BLOB,
            PersonalInfo TEXT,
            Status TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Chats (
            ChatID TEXT PRIMARY KEY,
            ChatName TEXT,
            ChatAmount INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ChatRelations (
            ChatID TEXT,
            UserID TEXT,
            UserAuthority INTEGER,
            FOREIGN KEY (ChatID) REFERENCES Chats (ChatID),
            FOREIGN KEY (UserID) REFERENCES Users (UserID)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Friends (
            User1 TEXT,
            User2 TEXT,
            Nickname1 TEXT,
            Nickname2 TEXT,
            FOREIGN KEY (User1) REFERENCES Users (UserID),
            FOREIGN KEY (User2) REFERENCES Users (UserID)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Messages (
            MessageID TEXT PRIMARY KEY,
            MessageContent TEXT,
            SenderID TEXT,
            ChatID TEXT,
            Time TIMESTAMP,
            MessageIndex INTEGER,
            FOREIGN KEY (SenderID) REFERENCES Users (UserID),
            FOREIGN KEY (ChatID) REFERENCES Chats (ChatID)
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # insert_user()
    # insert_chats()
