import sqlite3

# Set up the connection details
conn = sqlite3.connect('gesture_db.sqlite')
cursor = conn.cursor()

# Create the sign_language_detector table
cursor.execute('''CREATE TABLE IF NOT EXISTS sign_language_detector (
                    code_number INTEGER PRIMARY KEY,
                    image BLOB,
                    image_value VARCHAR(30),
                    date_of_storage DATE
                )''')

# Create the user_input_output table
cursor.execute('''CREATE TABLE IF NOT EXISTS user_input_output (
                    user_id INTEGER PRIMARY KEY,
                    user_name TEXT,
                    date DATE,
                    output VARCHAR(30),
                    image_id INTEGER,
                    FOREIGN KEY (image_id) REFERENCES sign_language_detector(code_number)
                )''')

# Commit the changes and close the connection
conn.commit()
conn.close()