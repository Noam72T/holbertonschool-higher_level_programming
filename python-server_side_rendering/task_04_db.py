from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    """Read and parse the JSON file"""
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    """Read and parse the CSV file"""
    products = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])  # Ensure the id is an integer
            row['price'] = float(row['price'])  # Ensure the price is a float
            products.append(row)
    return products

def read_sql():
    """Read and fetch data from the SQLite database"""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        products = []
        for row in rows:
            product = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products.append(product)
        conn.close()
        return products
    except sqlite3.Error as e:
        return None, str(e)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # Load the appropriate data source
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products, error = read_sql()
        if error:
            return render_template('product_display.html', error=f"Database error: {error}")

    # Filter by ID if provided
    if product_id:
        products = [p for p in products if p['id'] == product_id]

    # If no products are found, display a message
    if not products:
        return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
