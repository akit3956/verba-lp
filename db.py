import psycopg2
import psycopg2.extras
import bcrypt
import uuid
import os

def get_connection():
    try:
        import streamlit as st
        # If running inside Streamlit, prefer secrets
        database_url = st.secrets.get("DATABASE_URL", os.environ.get("DATABASE_URL"))
    except Exception:
        database_url = os.environ.get("DATABASE_URL")
        
    if not database_url:
        raise ValueError("DATABASE_URL is not set.")
        
    conn = psycopg2.connect(database_url)
    return conn

def init_db():
    conn = get_connection()
    c = conn.cursor()
    
    # Create the users table for PostgreSQL
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
    
    # Add columns if they do not exist
    c.execute("""
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name = 'users';
    """)
    columns = [row[0] for row in c.fetchall()]
    
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
    c.close()
    conn.close()

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def create_user(email, username, password, nationality):
    try:
        conn = get_connection()
        c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        if not email or not username or not password or not nationality:
            return False, "すべての項目を入力してください。"
            
        # Check if email exists
        c.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing = c.fetchone()
        
        if existing:
            c.close()
            conn.close()
            return False, "このメールアドレスは既に登録されています。"
            
        user_id = str(uuid.uuid4())
        hashed_pw = hash_password(password)
        # Founder's Pack gets 10000 VRB
        initial_bonus = 10000
        
        c.execute(
            'INSERT INTO users (id, email, username, password_hash, vrb_balance, nationality) VALUES (%s, %s, %s, %s, %s, %s)',
            (user_id, email, username, hashed_pw, initial_bonus, nationality)
        )
        conn.commit()
        return True, "登録が完了しました！学習アプリへログインできます。"
        
    except Exception as e:
        return False, f"エラーが発生しました: {e}"
        
    finally:
        if 'c' in locals():
            c.close()
        if 'conn' in locals():
            conn.close()

def get_all_users():
    conn = get_connection()
    c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        c.execute('SELECT id, email, username, nationality, created_at, vrb_balance FROM users ORDER BY created_at DESC')
    except psycopg2.OperationalError:
        conn.rollback()
        c.execute('SELECT id, email, username, nationality, vrb_balance FROM users')
       
    users = c.fetchall()
    c.close()
    conn.close()
    return [dict(row) for row in users]

def add_vrb_to_user(identifier, amount):
    conn = get_connection()
    c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    try:
        c.execute("SELECT id, vrb_balance FROM users WHERE email = %s OR username = %s", (identifier, identifier))
        user = c.fetchone()
        
        if not user:
            return False, f"User '{identifier}' not found."
            
        new_balance = user['vrb_balance'] + amount
        user_id = user['id']
        
        c.execute("UPDATE users SET vrb_balance = %s WHERE id = %s", (new_balance, user_id))
        
        # Log the transaction if transactions table exists
        c.execute("""
            SELECT count(*) 
            FROM information_schema.tables 
            WHERE table_name = 'transactions';
        """)
        table_exists = c.fetchone()[0] > 0
        
        if table_exists:
            c.execute(
                "INSERT INTO transactions (user_id, amount, type, description) VALUES (%s, %s, %s, %s)",
                (user_id, amount, 'admin_grant', 'Bulk VRB Issuance from Admin')
            )
            
        conn.commit()
        return True, f"Successfully added {amount:,.0f} VRB to {identifier}. New balance: {new_balance:,.0f}"
    except Exception as e:
        conn.rollback()
        return False, f"Error adding VRB: {e}"
    finally:
        if 'c' in locals():
            c.close()
        if 'conn' in locals():
            conn.close()
