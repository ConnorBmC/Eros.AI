import sqlite3

def update_knowledge(question, answer):
    # Connect to the database
    conn = sqlite3.connect('Knowledge.db')
    cursor = conn.cursor()

    # Insert a new record into the knowledge table
    cursor.execute('INSERT INTO knowledge (question, answer) VALUES (?, ?)', (question, answer))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Record added successfully!")

if __name__ == "__main__":
    # Example usage: Replace these with your actual question and answer
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    
    update_knowledge(question, answer)
