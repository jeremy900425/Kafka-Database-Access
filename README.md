# Kafka-Database-Access
## 檔案說明
### 需求描述.py -> 群組傳的 DB.py

### main.py -> 根目錄沒有.DB檔案時自動創建（呼叫init_DB檔案）、所有API路由都在此（共12支）

### SQL_Function.py -> 12支API之SQL操作都以函數的方式包在此檔案

```
根據需要可自由變更API路由內程式碼以及SQL_Function之內容
```



# topic name = UserID
# message = {SenderID, ReceiverID, ChatID, MessageContent, TimeStamp}

# Connect DB directly

# Create: Insert a new User with UserInfo
UserInfo = {UserID, UserName, Account, Password, Avatar, PersonalInfo, Status}
url = 'http://localhost:port/DB/Create_User'
response = requests.post(url, UserInfo)

# Update: Update UserInfo based on UserID
UserInfo = {UserID, UserName, Account, Password, Avatar, PersonalInfo, Status}
url = 'http://localhost:port/DB/Update_User'
response = requests.post(url, UserInfo)

# Query: Return wether the UserID exists.
url = 'http://localhost:port/DB/UserID_Exist'
response = requests.get(url, UserID)

# Query: Return wether the Account exists.
url = 'http://localhost:port/DB/Account_Exist'
response = requests.get(url, Account)

# Query: Return wether the ChatID exists.
url = 'http://localhost:port/DB/ChatID_Exist'
response = requests.get(url, ChatID)

# Create: Create a new chat with ChatInfo, ChatRelation
DB.Create_Chat()
ChatInfo = {ChatID, ChatName(私聊:default?=對方:暱稱, 群聊:default?=群組(1):群名, ),chatAmount = 1, chatStatus(定義私聊or群聊)}
ChatRelation = {ChatID, UserID(Creator), UserAuthority(1)}
url = 'http://localhost:port/DB/Create_Chat'
response = requests.post(url, ChatInfo, ChatRelation)

# Query: Return the UserID based on the Account
url = 'http://localhost:port/DB/Get_UserID'
response = requests.get(url, Account)

# Update: Update the ChatAmount
url = 'http://localhost:port/DB/Update_ChatAmount'
response = requests.post(url, ChatID, NewChatAmount)

# Create: Insert a new member to the chat
# ChatRelation is array of dictionary
ChatRelation = {ChatID, UserID, UserAuthority(0)}
url = 'http://localhost:port/DB/Add_Chat_Member'
response = requests.post(url, ChatRelation)

# Query: Return wether the user is in the group
url = 'http://localhost:port/DB/Group_Member_Exist'
response = requests.get(url, ChatID, UserID)

# Create: Insert the friend relation
Friend = {User1, User2, Nickname}
url = 'http://localhost:port/DB/Add_Friend'
response = requests.post(url, FriendInfo)
