from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS
from mysql.connector import Error

app = Flask(__name__)
CORS(app)

def get_database_tables(db_name):
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='0.0.0.0',
            port=3306,
            user='root',
            password='ConceptVine$@SX#21',
            database=db_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            return [table[0] for table in tables]
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
    return []

def get_table_schema(db_name, table_name):
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='0.0.0.0',
            port=3306,
            user='root',
            password='root',
            database=db_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"DESCRIBE `{table_name}`;")
            schema_details = cursor.fetchall()
            return [{'Field': field[0], 'Type': field[1], 'Null': field[2], 'Key': field[3], 'Default': field[4], 'Extra': field[5]} for field in schema_details]
    except Error as e:
        print(f"Error while connecting to MySQL to retrieve schema: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
    return []

@app.route('/schema/<db_name>', methods=['GET'])
def tables(db_name):
    tables = get_database_tables(db_name)
    return jsonify(tables)

@app.route('/schema/<db_name>/<table_name>', methods=['GET'])
def table_schema(db_name, table_name):
    print(table_name)
    schema = get_table_schema(db_name, table_name)
    return jsonify(schema)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
