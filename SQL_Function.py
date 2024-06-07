import base64
import sqlite3
from flask import Flask, request, jsonify
# Create a new user with UserInfo
def create_user(UserInfo):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("INSERT INTO Users (UserID, UserName, Account, Password, Avatar, PersonalInfo, Status) VALUES (?, ?, ?, ?, ?, ?, ?)", UserInfo)
  conn.commit()
  conn.close()

# Update UserInfo based on UserID
def update_user(UserInfo):
  user_id = UserInfo.get("UserID")
  user_name = UserInfo.get("UserName")
  account = UserInfo.get("Account")
  password = UserInfo.get("Password")
  avatar_base64 = UserInfo.get("Avatar")
  personal_info = UserInfo.get("PersonalInfo")
  status = UserInfo.get("Status")
  avatar = base64.b64decode(avatar_base64.split(',')[1]) if avatar_base64 else None
  conn = get_db_connection()
  cursor = conn.cursor()
  try:
      cursor.execute('''
          UPDATE Users
          SET UserName = ?, Account = ?, Password = ?, Avatar = ?, PersonalInfo = ?, Status = ?
          WHERE UserID = ?
      ''', (user_name, account, password, avatar, personal_info, status, user_id))
      conn.commit()
      if cursor.rowcount == 0:
          return jsonify({"error": "User not found"}), 404
      return jsonify({"status": "User updated successfully"}), 200
  except sqlite3.IntegrityError as e:
      return jsonify({"error": str(e)}), 500
  finally:
      conn.close()

# Check if Account exists
def check_account_exist(Account):
    account = Account
    print(account)
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT 1 FROM Users WHERE Account = ?
        ''', (account,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return jsonify({"exists": True}), 200
        else:
            return jsonify({"exists": False}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Check if ChatID exists
def check_chat_id_exist(ChatID):
    chatID = ChatID
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT 1 FROM Chats WHERE ChatID = ?
        ''', (chatID,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return jsonify({"exists": True}), 200
        else:
            return jsonify({"exists": False}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Get UserID based on Account
def get_user_id(Account):
    account = Account
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT UserID FROM Users WHERE Account = ?
        ''', (account,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return jsonify({"UserID": result["UserID"]}), 200
        else:
            return jsonify({"error": "Account not found"}), 404
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Add a new member to the chat
def add_chat_member(ChatRelation):
    chat_relation = ChatRelation
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        for relation in chat_relation:
            chat_id = relation.get("ChatID")
            user_id = relation.get("UserID")
            user_authority = relation.get("UserAuthority", 0)

            cursor.execute('''
                INSERT INTO ChatRelations (ChatID, UserID, UserAuthority)
                VALUES (?, ?, ?)
            ''', (chat_id, user_id, user_authority))

        conn.commit()
        return jsonify({"status": "Members added successfully"}), 201
    except sqlite3.IntegrityError as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Check if the user is in the group
def check_group_member_exist(ChatID, UserID):
    chat_id = ChatID
    user_id = UserID

    if not chat_id or not user_id:
        return jsonify({'error': 'Invalid input'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM ChatRelations WHERE ChatID = ? AND UserID = ?'
        (chat_id, user_id)
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        return jsonify({'exists': True}), 200
    else:
        return jsonify({'exists': False}), 200

# Insert the friend relation
def add_friend(FriendInfo):
    friend_info = FriendInfo
    user1 = friend_info.get("User1")
    user2 = friend_info.get("User2")
    nickname1 = friend_info.get("Nickname1")
    nickname2 = friend_info.get("Nickname2")

    if not user1 or not user2 or not nickname1 or not nickname2:
        return jsonify({"error": "Invalid input"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO Friends (User1, User2, Nickname1, Nickname2)
            VALUES (?, ?, ?, ?)
        ''', (user1, user2, nickname1, nickname2))
        conn.commit()
        return jsonify({"status": "Friend relation added successfully"}), 201
    except sqlite3.IntegrityError as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Create a new user with UserInfo
def create_user(UserInfo):

    user_tuple = (
        UserInfo["UserID"],
        UserInfo["UserName"],
        UserInfo["Account"],
        UserInfo["Password"],
        UserInfo["Avatar"],
        UserInfo["PersonalInfo"],
        UserInfo["Status"]
    )
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Users (UserID, UserName, Account, Password, Avatar, PersonalInfo, Status) VALUES (?, ?, ?, ?, ?, ?, ?)", user_tuple)
    
    conn.commit()
    conn.close()

# Check if UserID exists
def check_user_id_exist(UserID):

  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("SELECT COUNT(*) FROM Users WHERE UserID=?", (UserID,))
  result = cursor.fetchone()[0]
  conn.close()

  return result > 0


# Create a new chat with ChatInfo and ChatRelation
def create_chat(ChatInfo):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # 插入到 Chats 表
    chat_tuple = (
        ChatInfo["ChatID"],
        ChatInfo["ChatName"],
        ChatInfo["Amount"]
    )
    cursor.execute("INSERT INTO Chats (ChatID, ChatName, ChatAmount) VALUES (?, ?, ?)", chat_tuple)
    
    # 插入到 ChatRelations 表
    chat_relation_tuple = (
        ChatInfo["ChatRelation"]["ChatID"],
        ChatInfo["ChatRelation"]["UserID"],
        ChatInfo["ChatRelation"]["UserAuthority"]
    )
    cursor.execute("INSERT INTO ChatRelations (ChatID, UserID, UserAuthority) VALUES (?, ?, ?)", chat_relation_tuple)
    
    conn.commit()
    conn.close()



# Update ChatAmount
def update_chat_amount(ChatInfo):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("UPDATE Chats SET ChatAmount = ? WHERE ChatID = ?", (ChatInfo["Amount"], ChatInfo["ChatID"]))
    
    conn.commit()
    conn.close()




# Check if the user is in the group
def check_group_member_exist(UserID, ChatID):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT ROWID, ChatID, UserID, UserAuthority FROM ChatRelations WHERE UserID=? AND ChatID=?", (UserID, ChatID))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return {
            "UserAuthority": result[0],
            "UserID": result[1],
            "ChatID": result[2]
        }
    else:
        return None

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn