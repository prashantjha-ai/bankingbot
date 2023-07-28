import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
import openai
from database.connection import DatabaseConnection

class BankingBotTrain:
    def __init__(self):
        self.pipeline = self.build_pipeline()
        openai.api_key = 'sk-XwP94Yi4F9RzEYXtCibzT3BlbkFJ8XK7BI9STKm36OpBkL'
        self.db_connection = DatabaseConnection("localhost","5432","postgres")

    def process_input(self, user_input):
        intent = self.classify_intent(user_input)
        print("****************predicted_intent")
        print(intent)
        # Determine the intent of the user's input and send approprioate response
        if user_input.lower() in ["hello", "hi", "hey"]:
            response = "Hello! How can I assist you?"
        elif user_input.lower() in ["goodbye", "bye"]:
            response = "Goodbye! Have a great day!"
        elif user_input.lower() in ["thank you", "thanks"]:
            response = "You're welcome!"
        elif "?" in user_input:
            response = self.generate_ai_response(user_input)
        else:
            print("--in else")
            if intent == "balance":
                print("--in balance")
                response = self.handle_balance_intent()
            elif intent == "account info":
                response = self.handle_accountinfo_intent()
            elif intent == "transfer":
                response = self.handle_transfer_intent()
            elif intent == "payment":
                response = self.handle_payment_intent()
            elif intent == "help":
                response = self.handle_help_intent()
            else:
                print("--in Open ai")
                response = self.generate_ai_response(user_input)
        return response

    def build_pipeline(csv_file):
    # Load data from CSV into a pandas DataFrame
        data = pd.read_csv("dataset/banking_chatbot_dataset.csv")  # Assuming the CSV has two columns: 'text' and 'label'

        # Define the pipeline for intent classification
        pipeline = Pipeline([
            ("tfidf", TfidfVectorizer()),
            ("clf", LinearSVC())
        ])
        # Fit the pipeline to the training data
        pipeline.fit(data['text'], data['intent'])
        return pipeline

    def classify_intent(self, user_input):
        # Use the trained intent classification model to classify user input
        predicted_intent = self.pipeline.predict([user_input])

        return predicted_intent[0]

    def handle_balance_intent(self):
        # Will replace Logic for handling balance intent
        balance = self.get_account_balance_from_database()
        response = f"Your account balance is ${balance:.2f}."
        return response
    
    def handle_accountinfo_intent(self):
        # Will replace Logic for handling balance intent
        
        acc_info = self.get_account_info_from_database()
        response = (
            f"Account ID: {acc_info[0][0]}\n"
            f"Customer ID: {acc_info[0][1]}\n"
            f"Account Type: {acc_info[0][2]}\n"
            f"Account Balance: ${acc_info[0][3]:.2f}\n"
            f"Date: {acc_info[0][4]}\n"
            f"Status: {acc_info[0][5]}\n"
        )
        return response

    def handle_payment_intent(self):
        # Logic for handling transfer intent
        payment_info = self.get_payment_info_from_database()
        response = f"Payment info: {payment_info}"
        return response

    def handle_transfer_intent(self):
        # Will replace Logic for handling payment intent
        response = "To make a payment, please follow these steps..."
        return response

    def handle_help_intent(self):
        # Will replace Logic for handling help intent
        response = "How can I assist you? If you have any specific questions, feel free to ask."
        # Will replaces with help logic
        return response

    def generate_ai_response(self, user_input):
        # Use OpenAI GPT-3.5 model to generate AI response
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=50,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    
    def get_account_balance_from_database(self):
        # Establish the database connection first
        self.db_connection.connect()

        try:
            # Implement logic to fetch the account balance from the database
            # Use the DatabaseConnection class to execute the query and get the result
            query = "SELECT balance FROM accounts WHERE account_id = %s;"
            account_id = 3   # Replace with actual user_id or other parameters based on your database schema
            result = self.db_connection.execute_query(query, (account_id,))
            if result:
                return result[0][0]
            return 0.0  # Return a default value if balance not found
        finally:
            # Don't forget to disconnect from the database after the query
            self.db_connection.disconnect()

    def get_account_info_from_database(self):
        # Establish the database connection first
        self.db_connection.connect()

        try:
            # Implement logic to fetch the account balance from the database
            # Use the DatabaseConnection class to execute the query and get the result
            query = "SELECT * FROM accounts WHERE account_id = %s;"
            account_id = 3   # Replace with actual user_id or other parameters based on your database schema
            result = self.db_connection.execute_query(query, (account_id,))
            print("*******************************************")
            print(result)
            if result:
                return result
            return None  # Return a default value if balance not found
        finally:
            # Don't forget to disconnect from the database after the query
            self.db_connection.disconnect()

    def get_payment_info_from_database(self):
    # Establish the database connection first
        self.db_connection.connect()
        transaction_id = 2
        try:
            # Implement logic to fetch payment information from the database
            # Use the DatabaseConnection class to execute the query and get the result
            query = "SELECT transaction_type, amount, transaction_date FROM transactions WHERE transaction_id = %s;"
            result = self.db_connection.execute_query(query, (transaction_id,))
            if result:
                # Assuming the query returns a single row with payment_amount, payment_date, and payment_status
                transaction_type, amount, transaction_date = result[0]
                return {
                    "Payment Id": transaction_id,
                    "transaction Type": transaction_type,
                    "Amount": amount,
                    "Transaction Date": transaction_date,
                }
            return None  # Return None if payment information not found
        finally:
            # Don't forget to disconnect from the database after the query
            self.db_connection.disconnect()
