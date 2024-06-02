from flask import Flask, request, jsonify
import sqlite3
import os
from SQL_Function import *
from init_DB import init_db

app = Flask(__name__)

# Database setup

if not os.path.exists('database.db'):
    init_db()

# Routes
@app.route('/DB/Create_User', methods=['POST'])
def create_user_route():
    UserInfo = request.json
    create_user(UserInfo)
    return jsonify({"status": "User created successfully"}), 201

@app.route('/DB/Update_User', methods=['POST'])
def update_user_route():
    UserInfo = request.json
    update_user(UserInfo)
    return jsonify({"status": "User updated successfully"}), 200

@app.route('/DB/UserID_Exist', methods=['GET'])
def user_id_exist_route():
    UserID = request.args.get('UserID')
    exists = check_user_id_exist(UserID)
    return jsonify({"exists": exists}), 200

@app.route('/DB/Account_Exist', methods=['GET'])
def account_exist_route():
    Account = request.args.get('Account')
    exists = check_account_exist(Account)
    return jsonify({"exists": exists}), 200

@app.route('/DB/ChatID_Exist', methods=['GET'])
def chat_id_exist_route():
    ChatID = request.args.get('ChatID')
    exists = check_chat_id_exist(ChatID)
    return jsonify({"exists": exists}), 200

@app.route('/DB/Create_Chat', methods=['POST'])
def create_chat_route():
    data = request.json
    ChatInfo = data['ChatInfo']
    ChatRelation = data['ChatRelation']
    create_chat(ChatInfo, ChatRelation)
    return jsonify({"status": "Chat created successfully"}), 201

@app.route('/DB/Get_UserID', methods=['GET'])
def get_user_id_route():
    Account = request.args.get('Account')
    UserID = get_user_id(Account)
    return jsonify({"UserID": UserID}), 200

@app.route('/DB/Update_ChatAmount', methods=['POST'])
def update_chat_amount_route():
    data = request.json
    ChatID = data['ChatID']
    NewChatAmount = data['NewChatAmount']
    update_chat_amount(ChatID, NewChatAmount)
    return jsonify({"status": "Chat amount updated successfully"}), 200

@app.route('/DB/Add_Chat_Member', methods=['POST'])
def add_chat_member_route():
    ChatRelation = request.json
    add_chat_member(ChatRelation)
    return jsonify({"status": "Chat member added successfully"}), 201

@app.route('/DB/Group_Member_Exist', methods=['GET'])
def group_member_exist_route():
    ChatID = request.args.get('ChatID')
    UserID = request.args.get('UserID')
    exists = check_group_member_exist(ChatID, UserID)
    return jsonify({"exists": exists}), 200

@app.route('/DB/Add_Friend', methods=['POST'])
def add_friend_route():
    FriendInfo = request.json
    add_friend(FriendInfo)
    return jsonify({"status": "Friend added successfully"}), 201

if __name__ == '__main__':
    app.run(port=8080)
