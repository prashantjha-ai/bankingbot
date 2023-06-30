# Contains the main logic for your banking bot, such as handling user input, dialog flow, and responses.

# from bot.dialogs.account_dialog import AccountDialog
# from bot.dialogs.transaction_dialog import TransactionDialog
from bot.utils.train_Model import BankingBotTrain

BankingBotTrain = BankingBotTrain()


class BankingBot:
    def __init__(self):
        # Initialize an instance of BankingBot
        self.pipeline = BankingBotTrain.build_pipeline()

    def process_input(self, user_input):
        response = BankingBotTrain.process_input(user_input)
        return response

    def determine_intent(self, user_input):
        # Implement your logic to determine user's intent
        pass

