from flask import Flask, request, jsonify
import sqlite3
import os
from SQL_Function import *
from init_DB import init_db

app = Flask(__name__)

# Database setup

if not os.path.exists('database.db'):
    init_db()


@app.route('/DB/Update_User', methods=['POST'])
def update_user_route():
    UserInfo = request.json
    response, code = update_user(UserInfo)
    return response, code


@app.route('/DB/Account_Exist', methods=['GET'])
def account_exist_route():
    Account = request.args.get('Account')
    response, code = check_account_exist(Account)
    return response, code

@app.route('/DB/ChatID_Exist', methods=['GET'])
def chat_id_exist_route():
    ChatID = request.args.get('ChatID')
    response, code = check_chat_id_exist(ChatID)
    return response, code


@app.route('/DB/Get_UserID', methods=['GET'])
def get_user_id_route():
    account = request.args.get('Account')
    response, code = get_user_id(account)
    return  response, code

@app.route('/DB/Add_Chat_Member', methods=['POST'])
def add_chat_member_route():
    chat_relation = request.json
    response, code = add_chat_member(chat_relation)
    return response, code


    ChatID = request.args.get('ChatID')
    UserID = request.args.get('UserID')
    print(ChatID, UserID)
    response, code = check_group_member_exist(ChatID, UserID)
    return response, code

@app.route('/DB/Add_Friend', methods=['POST'])
def add_friend_route():
    friend_info = request.json
    response, code = add_friend(friend_info)
    return response, code

@app.route('/DB/Create_User', methods=['POST'])
def create_user_route():

    UserInfo = request.json

    print(UserInfo)
    create_user(UserInfo)
    
    return jsonify({"status": "User created successfully"}), 200


@app.route('/DB/UserID_Exist', methods=['GET'])
def UserID_Exist_route():

    user_id = request.args.get("UserID")
    
    if user_id is None:
        return jsonify({"status": "UserID not provided"}), 400
    
    exists = check_user_id_exist(user_id)
    result = {"exists": exists}

    return jsonify(result), 200


@app.route('/DB/Create_Chat', methods=['POST'])
def Create_Chat_route():

    ChatInfo = request.json

    print(ChatInfo)
    create_chat(ChatInfo)
    
    return jsonify({"status": "Chat created successfully"}), 200


@app.route('/DB/Update_ChatAmount', methods=['POST'])
def Update_ChatAmount_route():

    ChatInfo = request.json

    print(ChatInfo)
    update_chat_amount(ChatInfo)
    
    return jsonify({"status": "Update ChatAmount successfully"}), 200



@app.route('/DB/Group_Member_Exist', methods=['GET'])
def Group_Member_Exist_route():
    
    user_id = request.args.get("UserID")
    chat_id = request.args.get("ChatID")

    print(user_id)
    print(chat_id)
    
    if user_id is None or chat_id is None:
        return jsonify({"status": "UserID and ChatID are required"}), 400

    chat_relation = check_group_member_exist(user_id, chat_id)
    return jsonify(chat_relation), 200

if __name__ == '__main__':
    app.run(port=8080)
