# # Implements the dialog related to transactions, such as fund transfers, bill payments, etc.
#
#
# from bot.models.transaction_model import TransactionModel
# from bot.utils.validation import validate_transaction_amount
#
#
# class TransactionDialog:
#     def __init__(self):
#         self.transaction_model = TransactionModel()
#
#     def handle_dialog(self, user_input):
#         # Handle transaction-related dialog logic
#         action = user_input.strip().lower()
#
#         if action == "transfer":
#             return self.handle_transfer_dialog()
#         elif action == "payment":
#             return self.handle_payment_dialog()
#         else:
#             return "Unknown transaction. Please try again."
#
#     def handle_transfer_dialog(self):
#         # Handle transfer-specific dialog logic
#         recipient_account = input("Enter recipient's account number: ")
#         amount = input("Enter transfer amount: ")
#
#         if validate_transaction_amount(amount):
#             # Perform the transfer logic here
#             transaction_data = {
#                 "recipient_account": recipient_account,
#                 "amount": amount
#             }
#             self.transaction_model.perform_transfer(transaction_data)
#             return "Transfer successful."
#         else:
#             return "Invalid transfer amount."
#
#     def handle_payment_dialog(self):
#         # Handle payment-specific dialog logic
#         bill_type = input("Enter bill type: ")
#         amount = input("Enter payment amount: ")
#
#         if validate_transaction_amount(amount):
#             # Perform the payment logic here
#             transaction_data = {
#                 "bill_type": bill_type,
#                 "amount": amount
#             }
#             self.transaction_model.perform_payment(transaction_data)
#             return "Payment successful."
#         else:
#             return "Invalid payment amount."
#
