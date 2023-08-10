# conation all the common methods that are being used throughout project
from flask import session
import bot.bot


# class authentication:
def handle_authentication(user_input):
    """Handle authentication based on the current state."""
    # if session is not None:
    
    if session['state'] == 'AWAITING_USERNAME':
        session['username'] = user_input
        session['state'] = 'AWAITING_PASSWORD'
        return f"Please enter your Password for '{user_input}'"
    
    if session['state'] == 'AWAITING_PASSWORD':
        is_valid = bot.validate_credentials(session['username'], user_input)
        if is_valid:
            session['state'] = 'AUTHENTICATED'
            return "Welcome, How can I assist you today?"
        else:
            session['state'] = 'AWAITING_USERNAME'
            return "Invalid credentials. Please try again. Type your Username."
        
    session['state'] = 'AWAITING_USERNAME'
    return f"Please enter username"

    # def userinput():
    #     session['state'] == 'USERINPUT'
    #     return f"Please enter your username"