# from database.connection import DatabaseConnection
#
#
# def get_account_by_number(account_number):
#     db = DatabaseConnection(host="localhost", port=5432, dbname="banking", user="user", password="password")
#     db.connect()
#
#     query = "SELECT * FROM accounts WHERE account_number = %s"
#     result = db.execute_query(query, (account_number,))
#
#     db.disconnect()
#     if result:
#         # Process the result and return the account object
#         # pass
#     else:
#         return None
#
#
# def insert_transaction(transaction_data: object) -> object:
#     db = DatabaseConnection(host="localhost", port=5432, dbname="banking", user="user", password="password")
#     db.connect()
#
#     query = "INSERT INTO transactions (amount, ...) VALUES (%s, ...)"
#     db.execute_query(query, (transaction_data["amount"], ...))
#
#     db.disconnect()
