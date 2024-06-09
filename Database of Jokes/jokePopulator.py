import sqlite3

def create_database_and_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jokes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            joke TEXT NOT NULL,
            category TEXT NOT NULL
        )
    """)

def insert_jokes(cursor, jokes):
    insert_joke_query = "INSERT INTO jokes (joke, category) VALUES (?, ?)"
    cursor.executemany(insert_joke_query, jokes)

def automate(jokes, label):
    joke_with_label = [(joke.strip(), label) for joke in jokes]
    return joke_with_label

def read_jokes_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        jokes = file.readlines()
    return jokes

def main():
    # Read jokes from text files
    dad_jokes = read_jokes_from_file('dad_jokes.txt')
    sports_jokes = read_jokes_from_file('sports_jokes.txt')
    knock_knock_jokes = read_jokes_from_file('knock_knock_jokes.txt')

    # Automate labeling
    labeled_dad_jokes = automate(dad_jokes, 'Dad jokes')
    labeled_sports_jokes = automate(sports_jokes, 'Sports Jokes')
    labeled_knock_knock_jokes = automate(knock_knock_jokes, 'Knock Knock Jokes')

    # Combine all jokes
    all_jokes = labeled_dad_jokes + labeled_sports_jokes + labeled_knock_knock_jokes

    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('jokes.db')
    cursor = conn.cursor()

    # Create the database and table
    create_database_and_table(cursor)

    # Insert jokes into the table
    insert_jokes(cursor, all_jokes)

    # Commit the transaction
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

    print("Database and table created, and jokes inserted successfully.")

if __name__ == "__main__":
    main()
