from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS

models_src = Flask(__name__)
CORS(models_src)
db_config = {
    'host': '0.0.0.0',
    'user': 'root',
    'password': 'ConceptVine$@SX#21',
    'database': 'models'
}

@models_src.route('/get_aiuse_cases', methods=['GET'])
def get_aiuse_cases():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT Project_ID,Title,Notebook_Filename FROM aiusecase") 
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        use_cases = [{'AI_ID': row[0], 'ai_use_case_name': row[1],'notebook':row[2]} for row in rows]
        return jsonify(use_cases)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    models_src.run(host='0.0.0.0',debug=True,port=5006)