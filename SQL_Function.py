import sqlite3

# Create a new user with UserInfo
def create_user(UserInfo):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("INSERT INTO Users (UserID, UserName, Account, Password, Avatar, PersonalInfo, Status) VALUES (?, ?, ?, ?, ?, ?, ?)", UserInfo)
  conn.commit()
  conn.close()

# Update UserInfo based on UserID
def update_user(UserInfo):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("UPDATE Users SET UserName=?, Account=?, Password=?, Avatar=?, PersonalInfo=?, Status=? WHERE UserID=?", UserInfo)
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

# Check if Account exists
def check_account_exist(Account):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("SELECT COUNT(*) FROM Users WHERE Account=?", (Account,))
  result = cursor.fetchone()[0]
  conn.close()
  return result > 0

# Check if ChatID exists
def check_chat_id_exist(ChatID):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("SELECT COUNT(*) FROM Chats WHERE ChatID=?", (ChatID,))
  result = cursor.fetchone()[0]
  conn.close()
  return result > 0

# Create a new chat with ChatInfo and ChatRelation
def create_chat(ChatInfo, ChatRelation):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("INSERT INTO Chats (ChatID, ChatName, ChatAmount, ChatStatus) VALUES (?, ?, ?, ?)", ChatInfo)
  for relation in ChatRelation:
    cursor.execute("INSERT INTO ChatRelations (ChatID, UserID, UserAuthority) VALUES (?, ?, ?)", (relation['ChatID'], relation['UserID'], relation['UserAuthority']))
  conn.commit()
  conn.close()

# Get UserID based on Account
def get_user_id(Account):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("SELECT UserID FROM Users WHERE Account=?", (Account,))
  result = cursor.fetchone()
  conn.close()
  return result[0] if result else None

# Update ChatAmount
def update_chat_amount(ChatID, NewChatAmount):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("UPDATE Chats SET ChatAmount=? WHERE ChatID=?", (NewChatAmount, ChatID))
  conn.commit()
  conn.close()

# Add a new member to the chat
def add_chat_member(ChatRelation):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  for relation in ChatRelation:
    cursor.execute("INSERT INTO ChatRelations (ChatID, UserID, UserAuthority) VALUES (?, ?, ?)", (relation['ChatID'], relation['UserID'], relation['UserAuthority']))
  conn.commit()
  conn.close()

# Check if the user is in the group
def check_group_member_exist(ChatID, UserID):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("SELECT COUNT(*) FROM ChatRelations WHERE ChatID=? AND UserID=?", (ChatID, UserID))
  result = cursor.fetchone()[0]
  conn.close()
  return result > 0

# Insert the friend relation
def add_friend(FriendInfo):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  cursor.execute("INSERT INTO Friends (User1, User2, Nickname) VALUES (?, ?, ?)", FriendInfo)
  conn.commit()
  conn.close()
