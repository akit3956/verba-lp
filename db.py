import sqlite3
import bcrypt
import uuid
from datetime import datetime
import os

# Point to the main app's database if possible, else fallback to local users.db for Streamlit Cloud
main_db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "jlpt_app", "backend", "jlpt.db")
if os.path.exists(main_db_path):
    DB_FILE = main_db_path
else:
    DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.db")

def get_connection():
    # check_same_thread=False is needed for Streamlit since it runs across multiple threads
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    c = conn.cursor()
    
    # Create the table if it's running locally/standalone and doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            username TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            vrb_balance INTEGER DEFAULT 0,
            nationality TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Ensure legacy columns exist just in case
    c.execute("PRAGMA table_info(users)")
    columns = [column[1] for column in c.fetchall()]
    
    if "nationality" not in columns:
        try:
            c.execute("ALTER TABLE users ADD COLUMN nationality TEXT")
        except:
            pass
            
    if "created_at" not in columns:
        try:
            c.execute("ALTER TABLE users ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
        except:
            pass
            
    conn.commit()
    conn.close()

def hash_password(password):
    # Use bcrypt to match the main app's auth
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def create_user(email, username, password, nationality):
    conn = get_connection()
    c = conn.cursor()
    
    # Simple validation
    if not email or not username or not password or not nationality:
        return False, "すべての項目を入力してください。"
        
    # Check if email exists
    existing = c.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    if existing:
        conn.close()
        return False, "このメールアドレスは既に登録されています。"
        
    try:
        user_id = str(uuid.uuid4())
        hashed_pw = hash_password(password)
        # Founder's Pack gets 10000 VRB
        initial_bonus = 10000
        
        c.execute(
            'INSERT INTO users (id, email, username, password_hash, vrb_balance, nationality) VALUES (?, ?, ?, ?, ?, ?)',
            (user_id, email, username, hashed_pw, initial_bonus, nationality)
        )
        conn.commit()
        return True, "登録が完了しました！学習アプリへログインできます。"
    except Exception as e:
        return False, f"エラーが発生しました: {e}"
    finally:
        conn.close()

def get_all_users():
    conn = get_connection()
    c = conn.cursor()
    # Fetch all users, ordering by created_at if it exists, otherwise id
    try:
        c.execute('SELECT id, email, username, nationality, created_at, vrb_balance FROM users ORDER BY created_at DESC')
    except sqlite3.OperationalError:
       c.execute('SELECT id, email, username, nationality, vrb_balance FROM users')
       
    users = c.fetchall()
    conn.close()
    
    # Convert to list of dicts for easier use in pandas DataFrame
    return [dict(row) for row in users]

def add_vrb_to_user(identifier, amount):
    """
    Adds a specific amount of VRB to a user's balance.
    The identifier can be an email or username.
    """
    conn = get_connection()
    c = conn.cursor()
    
    try:
        # Check if user exists by email or username
        c.execute("SELECT id, vrb_balance FROM users WHERE email = ? OR username = ?", (identifier, identifier))
        user = c.fetchone()
        
        if not user:
            return False, f"User '{identifier}' not found."
            
        new_balance = user['vrb_balance'] + amount
        user_id = user['id']
        
        # Update balance
        c.execute("UPDATE users SET vrb_balance = ? WHERE id = ?", (new_balance, user_id))
        
        # Log the transaction (if there is a transactions table, otherwise skip. Main app has one)
        c.execute("PRAGMA table_info(transactions)")
        if len(c.fetchall()) > 0:
            c.execute(
                "INSERT INTO transactions (user_id, amount, type, description) VALUES (?, ?, ?, ?)",
                (user_id, amount, 'admin_grant', 'Bulk VRB Issuance from Admin')
            )
            
        conn.commit()
        return True, f"Successfully added {amount:,.0f} VRB to {identifier}. New balance: {new_balance:,.0f}"
    except Exception as e:
        return False, f"Error adding VRB: {e}"
    finally:
        conn.close()
