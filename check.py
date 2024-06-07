import sqlite3

def get_foreign_keys(db_path, table_name):
    # 連接到SQLite資料庫
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 查詢外鍵資訊
    cursor.execute(f"PRAGMA foreign_key_list({table_name})")
    foreign_keys = cursor.fetchall()

    # 關閉資料庫連接
    conn.close()

    return foreign_keys

def main():
    db_path = 'database.db'  # 資料庫檔案的路徑
    table_name = 'Messages'       # 想要查詢的表名

    foreign_keys = get_foreign_keys(db_path, table_name)
    
    if not foreign_keys:
        print(f"No foreign keys found for table {table_name}")
    else:
        for fk in foreign_keys:
            print(f"Foreign Key ID: {fk[0]}")
            print(f"From Column: {fk[3]}")
            print(f"References Table: {fk[2]}")
            print(f"References Column: {fk[4]}")
            print("---")

if __name__ == "__main__":
    main()
