from datetime import datetime
import sqlite3
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Database connection helper


def get_db_connection():
  conn = sqlite3.connect('database.db')
  conn.row_factory = sqlite3.Row
  return conn


# Initialize Database Table
def init_db():
  conn = get_db_connection()
  conn.execute(
      'CREATE TABLE IF NOT EXISTS expenses ('
      'id INTEGER PRIMARY KEY AUTOINCREMENT, '
      'title TEXT NOT NULL, '
      'amount REAL NOT NULL, '
      'type TEXT NOT NULL, '
      'category TEXT NOT NULL, '
      'date TEXT NOT NULL)'
  )
  conn.commit()
  conn.close()


init_db()


# Route to serve frontend
@app.route('/')
def index():
  return render_template('index.html')


# API: Get all transactions
@app.route('/api/transactions', methods=['GET'])
def get_transactions():
  conn = get_db_connection()
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
  rows = cursor.fetchall()
  conn.close()

  transactions = []
  for row in rows:
    transactions.append({
        'id': row['id'],
        'title': row['title'],
        'amount': row['amount'],
        'type': row['type'],
        'category': row['category'],
        'date': row['date'],
    })
  return jsonify(transactions)


# API: Add new transaction
@app.route('/api/transactions', methods=['POST'])
def add_transaction():
  data = request.json
  title = data.get('title')
  amount = data.get('amount')
  t_type = data.get('type')
  category = data.get('category')
  date = data.get('date', datetime.now().strftime('%Y-%m-%d'))

  # Server-side validation
  if not title or amount is None or t_type not in ['income', 'expense']:
    return jsonify({'error': 'Invalid input data'}), 400

  try:
    amount = float(amount)
    if amount <= 0:
      raise ValueError()
  except ValueError:
    return jsonify({'error': 'Amount must be a positive number'}), 400

  conn = get_db_connection()
  cursor = conn.cursor()
  cursor.execute(
      'INSERT INTO expenses (title, amount, type, category, date) VALUES (?,'
      ' ?, ?, ?, ?)',
      (title, amount, t_type, category, date),
  )
  conn.commit()
  new_id = cursor.lastrowid
  conn.close()

  return jsonify({
      'id': new_id,
      'title': title,
      'amount': amount,
      'type': t_type,
      'category': category,
      'date': date,
  }), 201


# API: Delete transaction
@app.route('/api/transactions/<int:id>', methods=['DELETE'])
def delete_transaction(id):
  conn = get_db_connection()
  cursor = conn.cursor()
  cursor.execute('DELETE FROM expenses WHERE id = ?', (id,))
  conn.commit()
  conn.close()
  return jsonify({'success': True})


if __name__ == '__main__':
  app.run(debug=True)