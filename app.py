from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_password(name):
    letter_alternatives = {
        'a': '@', 'b': '8', 'c': '(', 'd': '|)', 'e': '3', 'f': '|=', 'g': '9',
        'h': '#', 'i': '!', 'j': '_|', 'k': '|<', 'l': '1', 'm': '|\\/|',
        'n': '|\\|', 'o': '0', 'p': '|*', 'q': 'O_', 'r': '|2', 's': '$',
        't': '7', 'u': '|_|', 'v': '\\/', 'w': '\\/\\/', 'x': '><', 'y': '`/',
        'z': '2'
    }

    password = ''
    for letter in name.lower():
        if letter.isalpha() and random.random() < 0.5:
            if letter in letter_alternatives:
                password += letter_alternatives[letter]
            else:
                password += letter
        else:
            password += letter

    for _ in range(3):
        password += str(random.randint(0, 9))

    return password

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/generate', methods=['POST'])
def generate():
    input_name = request.form['name-input']
    generated_password = generate_password(input_name)
    return render_template('index.html', generated_password=generated_password, input_name=input_name)

if __name__ == '__main__':
    app.run(debug=True)
