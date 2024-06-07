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

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def insert_user():
    # 示例数据
    user_id = "00000000-0000-0000-0000-000000000000"
    user_name = "test"
    account = "test"
    password = "test"
    avatar_base64 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/wcAAgMBAgJZfxsAAAAASUVORK5CYII="
    personal_info = "test"
    status = "test"
    
    # 解码Base64编码的头像数据
    avatar = base64.b64decode(avatar_base64.split(',')[1])

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(f'''
            INSERT INTO Users (UserID, UserName, Account, Password, Avatar, PersonalInfo, Status)
            VALUES ('{user_id}', '{user_name}', '{account}', '{password}', ?, '{personal_info}', '{status}')
        ''', (avatar,))
        conn.commit()
        print("User inserted successfully")
    except sqlite3.IntegrityError as e:
        print(f"Error inserting user: {e}")
    finally:
        conn.close()


def insert_chats():
    chatID = "00000000-0000-0000-0000-000000000000"
    chatName = "test"
    Amount = 123

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(f'''
            INSERT INTO Chats (ChatID, ChatName, ChatAmount)
            VALUES ('{chatID}', '{chatName}', '{Amount}')
        ''')
        conn.commit()
        print("User caht successfully")
    except sqlite3.IntegrityError as e:
        print(f"Error inserting caht: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    # insert_user()
    insert_chats()
