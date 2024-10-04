from flask import Flask, render_template, request, jsonify
import sqlite3
import requests  # Only include if you are making requests

app = Flask(__name__)

def get_response(query):
    conn = sqlite3.connect('Knowledge.db')
    cursor = conn.cursor()
    cursor.execute('SELECT response FROM knowledge WHERE query = ?', (query,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "I'm sorry, I don't know the answer to that."

@app.route('/')
def home():
    return render_template('eros_ai.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message']
    response = get_response(user_input)
    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)
