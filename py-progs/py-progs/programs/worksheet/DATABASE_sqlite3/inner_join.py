import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
# Perform an inner join on the 'customer_id' column
with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()

    result = cursor.execute('''
        SELECT customers.customer_id, customers.name, customers.email, orders.product, orders.quantity
        FROM customers
        INNER JOIN orders ON customers.customer_id = orders.customer_id
    ''')

    # Fetch and print the results
    print("Results of INNER JOIN:")
    for row in result:
        print(row)
