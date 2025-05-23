# API Requests 
# Use functions from services.py - extract_calculate, convert_csv_to_json
import csv
from flask import Blueprint, jsonify, request
from .services import convert_csv_to_json, extract_calculate
from .db_repo import insert_db
import logging



views_bp = Blueprint('views',__name__)

# @views_bp.route('/', methods=['POST'])
# def home():
#     return jsonify({"message":"Welcome to the Student Marks API!"})
# # Upload API



@views_bp.route('/upload', methods=['POST'])
def upload_data():
    try:
        #If request contains file-
        if 'file' in request.files:
            file = request.files['file']
            raw_data = file.read()
            print(raw_data)
            name=file.filename.lower()
            if name.endswith('.csv'): 
                is_csv=True
                print("CSV file detected")
                # return jsonify({"success": "csv accepted"}),200
            else: # Fallback if not CSV
                return jsonify({"error": "Invalid file format. Only CSV files are accepted."}),400
            
        else: 
            #If not file, check raw data 
            raw_data=request.get_data()
            logging.info(("Raw data received: %s", raw_data))
            is_csv = False
            if not raw_data:
                return jsonify({"error": "Data not provided."},400)

        data = convert_csv_to_json(raw_data, is_csv=is_csv) 
        print(data)# is_csv is True/False based on above code
        if not data:
            return jsonify({"error":"No data found."}),400
        print("Data recieved:",data)
        details = extract_calculate(data)
        if not details: 
            return jsonify({"error":"Could not extract data."}),400


        success = insert_db(details)
        if success:
            return jsonify({"message":"Data insertion successful,"}),400
        if not success:
            return jsonify({"error":"Could not insert into database."})
    except Exception as e:
        logging.error("Error in upload_data: %s", str(e) + "line number:"+str(e.__traceback__.tb_lineno))
        return jsonify({"error": "An error occurred while processing the request."}), 500

