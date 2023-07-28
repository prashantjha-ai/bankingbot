# Contains functions for input validation, data formatting, etc.
# You can add more utility files as needed.

# def authenticate_user(self, username, password):
#     # Implement logic to authenticate the user from the database
#     # Use the DatabaseConnection class to execute the query and get the result
#     self.db_connection.connect()

#     query = "SELECT COUNT(*) FROM login WHERE username = %s AND password = %s;"
#     result = self.db_connection.execute_query(query, (username, password))
#     if result and result[0][0] == 1:
#         return True
#     return False
def validate_account_number(account_number):
    # Implement your account number validation logic
    pass


def validate_transaction_amount(amount):
    # Implement your transaction amount validation logic
    pass
