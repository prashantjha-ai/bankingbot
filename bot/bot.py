# Contains the main logic for your banking bot, such as handling user input, dialog flow, and responses.

# from bot.dialogs.account_dialog import AccountDialog
# from bot.dialogs.transaction_dialog import TransactionDialog
from bot.utils.train_Model import BankingBotTrain
from database.connection import DatabaseConnection

BankingBotTrain = BankingBotTrain()


class BankingBot:
    def __init__(self):
        # Initialize an instance of BankingBot
        self.pipeline = BankingBotTrain.build_pipeline()

    def validate_credentials(self, username, password):
        self.db_connection = DatabaseConnection("localhost","5432","postgres")
        self.db_connection.connect()

        query = "SELECT COUNT(*) FROM login WHERE username = %s AND password = %s;"
        result = self.db_connection.execute_query(query, (username, password))
        if result and result[0][0] == 1:
            return True
        return False

    def process_input(self, user_input):
        response = BankingBotTrain.process_input(user_input)
        return response

    def determine_intent(self, user_input):
        # Implement your logic to determine user's intent
        pass

