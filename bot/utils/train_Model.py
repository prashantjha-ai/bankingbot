from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
import openai


class BankingBotTrain:
    def __init__(self):
        self.pipeline = self.build_pipeline()
        openai.api_key = 'We will use our OpenAIAPI'

    def process_input(self, user_input):
        intent = self.classify_intent(user_input)

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
            if intent == "balance":
                response = self.handle_balance_intent()
            elif intent == "transfer":
                response = self.handle_transfer_intent()
            elif intent == "payment":
                response = self.handle_payment_intent()
            elif intent == "help":
                response = self.handle_help_intent()
            else:
                response = self.generate_ai_response(user_input)

        return response

    def build_pipeline(self):
        # Define the pipeline for intent classification
        pipeline = Pipeline([
            ("tfidf", TfidfVectorizer()),
            ("clf", LinearSVC())
        ])

        # Example training data
        training_data = [
            ("What is my account balance?", "balance"),
            ("Can I transfer money to another account?", "transfer"),
            ("How do I make a payment?", "payment"),
            ("Help me with my account", "help"),
            # Add more labeled examples...
        ]

        # Fit the pipeline to the training data
        pipeline.fit([x[0] for x in training_data], [x[1] for x in training_data])

        return pipeline

    def classify_intent(self, user_input):
        # Use the trained intent classification model to classify user input
        predicted_intent = self.pipeline.predict([user_input])
        return predicted_intent[0]

    def handle_balance_intent(self):
        # Will replace Logic for handling balance intent
        response = "Your account balance is $X."
        return response

    def handle_transfer_intent(self):
        # Logic for handling transfer intent
        response = "To initiate a transfer, please provide the necessary details."
        return response

    def handle_payment_intent(self):
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
