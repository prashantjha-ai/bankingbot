from flask import Flask, render_template, request
from bot.bot import BankingBot


app = Flask(__name__)
bot = BankingBot()


@app.route('/')
def home():
    chat_history = []  # Initialize an empty chat history
    response = "Type your Username"  # Welcome message
    return render_template('index.html', response=response, chat_history=chat_history)


# @app.route('/submit', methods=['POST'])
# def submit():
#     user_input = request.form['user_input']
#     chat_history_str = request.form.get('chat_history', '[]')
#     chat_history = eval(chat_history_str)

#     response = bot.process_input(user_input)
#     chat_history.append(user_input)
#     chat_history.append(response)

#     return render_template('index.html', response=response, chat_history=chat_history)

@app.route('/submit', methods=['POST'])
def submit():
    
    user_input = request.form['user_input']
    chat_history_str = request.form.get('chat_history', '[]')
    chat_history = eval(chat_history_str)
    # print("Without appending2")
    # print(chat_history)

    if 'username' not in chat_history:
        chat_history.append('username')  # Indicate that we are expecting a username
        response = "Please enter your Username"
        # print("after append username and provideing response")
        # print(chat_history)
        
    elif 'password' not in chat_history:
        # Check if the provided username exists in the "users" list
        provided_username = user_input.strip()
    #     if any(user.username == provided_username for user in users):
        chat_history.append('password')  # Indicate that we are expecting a password
        response = "Please enter your Password for '{}'".format(provided_username)
        # print("after append password and provideing response")
        # print(chat_history)
    #     else:
    #         response = "Invalid Username. Please enter a valid Username."
    elif 'Welcome, How can I assist you today?' not in chat_history:
        # Now we have both username and password in chat_history
    
        provided_password = user_input.strip()
        provided_username = chat_history[-2].strip()  # Retrieve the last added username
        # Check if the provided credentials are valid
        print(provided_username, provided_password)
        if bot.validate_credentials(provided_username, provided_password):
            response = "Welcome, How can I assist you today?"
        else:
            response = "Invalid credentials. Please try again with correct Username and Password."
    else:
        print(chat_history[-2].strip())
        response = bot.process_input(user_input)
    chat_history.append(user_input)
    chat_history.append(response)


    return render_template('index.html', response=response, chat_history=chat_history)



if __name__ == '__main__':
    app.run(debug=True)
