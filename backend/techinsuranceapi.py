from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
import mysql.connector

app = Flask(__name__)
api = Api(app, version='1.0', title='Insurance APIs', description='API for managing insurance data')

# Database Configuration
db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'techinsurance'
}

# Function to connect to MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Exception as e:
        print("Error connecting to database:", e)



ns_insurer = api.namespace('insurer',description='<h1 style="font-weight:bold; font-size:4px;"></h1>')
@ns_insurer.route('/vehicle')
class VehicleResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all vehicle data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM vehicle")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
        
@ns_insurer.route('/insert/vehicle')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the vehicle table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO vehicle ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400



# Define similar routes for other table names...
@ns_insurer.route('/claim')
class ClaimResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all claim data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM claim")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
        
@ns_insurer.route('/insert/claim')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the claim table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO claim ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400

        
@ns_insurer.route('/driver')
class DriverResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all driver data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM driver")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
        

@ns_insurer.route('/insert/driver')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the driver table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO driver ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400



# Define similar routes for other table names
@ns_insurer.route('/beneficiary')
class BeneficiaryResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all beneficiaries')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM beneficiary")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
        # Logic to get beneficiaries from the database
            return jsonify({'success': True, 'data': 'Beneficiary data'})
        
@ns_insurer.route('/insert/beneficiary')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the beneficiary table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO beneficiary ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400




# Define resources for each endpoint
@ns_insurer.route('/address')
class AddressResource(Resource):
    @api.doc(description='### Addresses\nGet all addresses')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM address")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
        
@ns_insurer.route('/insert/address')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the address table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO address ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400




# Define similar routes for other tables...
@ns_insurer.route('/conviction')
class ConvictionResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all conviction data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM conviction")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
        
@ns_insurer.route('/insert/conviction')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the conviction table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO conviction ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400

        
# Define similar routes for other tables...
@ns_insurer.route('/drivinglicence')
class DrivingLicenceResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all driving licence data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM drivinglicence")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
        
@ns_insurer.route('/insert/drivinglicence')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the drivinglicence table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO drivinglicence ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400


ns_insurance = api.namespace('insurance',description='<h1 style="font-weight:bold; font-size:4px;"></h1>')

@ns_insurance.route('/motorcoverage')
class MotorCoverageResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all motor coverage data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM motorcoverage")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
        

@ns_insurance.route('/insert/motorcoverage')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the motorcoverage table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO motorcoverage ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400


        
   
@ns_insurance.route('/insuranceentity')
class InsuranceEntityResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all insurance entity data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM insuranceentity")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
        
@ns_insurance.route('/insert/insuranceentity')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the insuranceentity table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO insuranceentity ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400
        

@ns_insurance.route('/personal')
class PersonalResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all personal data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM personal")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
        
@ns_insurance.route('/insert/personal')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the personal table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO personal ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400
        



@ns_insurance.route('/commercial')
class CommercialResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all commercial data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM commercial")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
        # Logic to get commercial data from the database
            return jsonify({'success': True, 'data': 'Commercial data'})


@ns_insurance.route('/insert/commercial')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the commercial table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO commercial ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400
        

@ns_insurance.route('/product')
class ProductResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all product data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM product")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})
        


@ns_insurance.route('/insert/product')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the product table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO product ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400


@ns_insurance.route('/premiumbordereau')
class PremiumBordereauResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all premium bordereau data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM premiumbordereau")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})


@ns_insurance.route('/insert/premiumbordereau')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the premiumbordereau table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO premiumbordereau ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400
        

@ns_insurance.route('/claimsbordereau')
class ClaimsBordereauResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all claims bordereau')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM claimsbordereau")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
        # Logic to get claims bordereau from the database
            return jsonify({'success': True, 'data': 'Claims bordereau data'})


@ns_insurance.route('/insert/claimsbordereau')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the claimsbordereau table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO claimsbordereau ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400
        

# Define similar routes for other tables...
@ns_insurance.route('/conviction')
class ConvictionResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all conviction data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM conviction")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})

@ns_insurance.route('/insert/conviction')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the conviction table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO conviction ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400



# Define similar routes for other tables...
@ns_insurance.route('/insuranceentity')
class InsuranceEntityResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all insurance entity data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM insuranceentity")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})


@ns_insurance.route('/insert/insuranceentity')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the insuranceentity table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO insuranceentity ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400

# Define similar routes for other tables...
@ns_insurance.route('/medicalcondition')
class MedicalConditionResource(Resource):
    @api.doc(responses={200: 'OK'}, description='Get all medical condition data')
    def get(self):
        try:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM medicalcondition")
                rows = cursor.fetchall()
                cursor.close()
                connection.close()
                return jsonify({'success': True, 'data': rows})
            else:
                return jsonify({'success': False, 'message': 'Failed to connect to the database'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})


@ns_insurance.route('/insert/medicalcondition')
class AddressResourceInsert(Resource):
    @api.doc(responses={201: 'Created', 400: 'Bad Request'}, description='Insert a new record into the medicalcondition table')
    def post(self):
        try:
            data = request.get_json()
            if not isinstance(data, dict):
                return {'success': False, 'message': 'Invalid JSON format'}, 400

            # Connect to the database
            connection = connect_to_db()
            if not connection:
                return {'success': False, 'message': 'Failed to connect to database'}, 500

            cursor = connection.cursor()
            column_names = list(data.keys())
            column_values = list(data.values())
            placeholders = ', '.join(['%s' for _ in range(len(column_names))])
            query = f"INSERT INTO medicalcondition ({', '.join(column_names)}) VALUES ({placeholders})"
            cursor.execute(query, column_values)
            connection.commit()
            cursor.close()
            connection.close()

            return {'success': True, 'message': 'Record inserted successfully'}, 201
        except Exception as e:
            return {'success': False, 'message': str(e)}, 400



database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='test_db'
)

# def connect_to_db_oip():
#     db_config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'password': 'root',
#     'database': 'oip'
#     }
#     try:
#         connection = mysql.connector.connect(**db_config)
#         return connection
#     except Exception as e:
#         print("Error connecting to database:", e)


# @contextmanager
# def get_db_connection():
#     conn = database.connect()
#     # try:
#     yield conn
#     # finally:
#     #     conn.close()


# Generate a random OTP
def generate_otp():
    return str(random.randint(1000, 9999))

# Send OTP to the specified email address
def send_otp(email, otp):
    sender_email = "oipmakeyourown@gmail.com"
    sender_password = "vvrd tais gzrz krqf"
    subject = "OTP for verification"
    message = f"Your OTP for verification is: {otp}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("Error sending email:", str(e))
        return False
 
@app.route('/send_otp', methods=['POST'])
def send_otp_route():
    cursor = database.cursor()
    email = request.json.get('email')
    if not email:
        return jsonify({'error': 'Email address not provided'}), 400
 
    otp = generate_otp()
    if send_otp(email, otp):
        cursor.execute("INSERT INTO otp (otp_value, used,email) VALUES (%s, %s,%s)", (otp,0,email))
        database.commit()
        return jsonify({'message': 'OTP sent successfully'}), 200
    else:
        return jsonify({'error': 'Failed to send OTP'}), 500

@app.route('/login', methods=['POST'])
def login():
    cursor = database.cursor(dictionary=True)  # Ensure dictionary=True for fetching results as dictionaries

    # Get email and password from the request
    email = request.json.get('email')
    password = request.json.get('password')

    # Check if email and password are provided
    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    # Query the database to check if the user exists
    try:
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
    except mysql.connector.Error as err:
        return jsonify({'error': f'Database error: {str(err)}'}), 500

    # If user is not found or password doesn't match, return error
    if not user or user['password'] != password:
        return jsonify({'error': 'Invalid username or password'}), 401

    return jsonify({'message': 'Login successful'}), 200

# Endpoint for updating password
@app.route('/update_password', methods=['POST'])
def update_password():
    cursor = database.cursor()

    email = request.json.get('email')
    new_password = request.json.get('new_password')

    if not email or not new_password:
        return jsonify({'error': 'Email and new password are required'}), 400

    # Update the password in the database
    cursor.execute("UPDATE users SET password = %s WHERE email = %s", (new_password, email))
    database.commit()

    return jsonify({'message': 'Password updated successfully'}), 200

@app.route('/check_email', methods=['POST'])
def check_email():
    data = request.get_json()  # Get data as JSON
    email = data.get('email')
    
    if email:
        cursor = database.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            result = cursor.fetchone()
            database.commit()
            if result:
                return jsonify({'exists': True}), 200  # Email exists
            else:
                return jsonify({'exists': False}), 404  # Email not found
        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Internal server error
    else:
        return jsonify({'error': 'Email parameter is missing'}), 400  # Bad request



# Endpoint for adding a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    cursor = database.cursor()
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({'error': 'All fields are required'}), 400

    # Check if the user already exists
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    if cursor.fetchone():
        return jsonify({'error': 'User already exists'}), 400

    # Add the new user to the database
    cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
    database.commit()

    return jsonify({'message': 'User added successfully'}), 200


# API endpoint to validate OTP
@app.route('/validate_otp', methods=['POST'])
def validate_otp():
    data = request.json
    otp = data.get('otp')
    email = request.json.get('email')
    password = request.json.get('password')

    if not otp:
        return jsonify({'error': 'OTP not provided'}), 400

    # Connect to MySQL database
    try:
        cursor = database.cursor()

        # Check if the OTP exists in the database and is not already used
        query = "SELECT * FROM otp WHERE otp_value = %s AND used = FALSE AND email = %s"
        cursor.execute(query, (otp,email))
        otp_entry = cursor.fetchone()

        if otp_entry:
            # Mark the OTP as used
            update_query = "UPDATE otp SET used = TRUE WHERE id = %s"
            cursor.execute(update_query, (otp_entry[0],))  # Assuming id is the first column
            cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
            database.commit()
            return jsonify({'message': 'OTP is valid'}), 200

        else:
            return jsonify({'error': 'Invalid OTP or OTP already used'}), 400

    except mysql.connector.Error as e:
        return jsonify({'error': f'Error accessing database: {str(e)}'}), 500
    

# datasets.py  

def get_database_tables_for_datasets(db_name):
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',
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

def get_table_schema_for_datasets(db_name, table_name):
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
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
    tables = get_database_tables_for_datasets(db_name)
    return jsonify(tables)

@app.route('/schema/<db_name>/<table_name>', methods=['GET'])
def table_schema(db_name, table_name):
    print(table_name)
    schema = get_table_schema_for_datasets(db_name, table_name)
    return jsonify(schema)


# models.py


def get_db_connection_for_models():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'models'
    }
    return mysql.connector.connect(**db_config)

@app.route('/get_aiuse_cases', methods=['GET'])
def get_aiuse_cases():
    try:
        conn = get_db_connection_for_models()
        cursor = conn.cursor()
        cursor.execute("SELECT Project_ID, Title, Notebook_Filename FROM aiusecase") 
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        use_cases = [{'AI_ID': row[0], 'ai_use_case_name': row[1], 'notebook': row[2]} for row in rows]
        return jsonify(use_cases)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# solution.py


def get_db_connection_for_solution():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'test_db'
    }
    return mysql.connector.connect(**db_config)

@app.route('/get_use_cases1', methods=['GET'])
def get_use_cases1():
    try:
        conn = get_db_connection_for_solution()
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
    app.run(debug=True,port=5050)
