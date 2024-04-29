from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS

solution_src = Flask(__name__)
CORS(solution_src)
db_config = {
    'host': '0.0.0.0',
    'user': 'root',
    'password': 'ConceptVine$@SX#21',
    'database': 'test_db'
}


@solution_src.route('/get_use_cases1', methods=['GET'])
def get_use_cases1():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT UC_ID, Use_Case FROM bausecase")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        use_cases = [{'UCID': row[0], 'use_case_name': row[1]} for row in rows]
        return jsonify(use_cases)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    solution_src.run(host='0.0.0.0',debug=True,port=5005)


