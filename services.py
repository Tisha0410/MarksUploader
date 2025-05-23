import csv 
from flask import jsonify,request
from io import StringIO
import logging
import json 

def convert_csv_to_json(data, is_csv=False):
     """Accepts raw data. If is_csv = True, convert to list in JSON format."""
    # Read the CSV file
     if is_csv:
        #if data is in csv (bytes) format
        if isinstance(data, bytes):
            data = data.decode('utf-8') #bytes to string
            data = StringIO(data) #string to StringIO (file-like object)
            reader = csv.DictReader(data) #csv read line-to-line - first row: header, subsequent rows: dict data
            return list(reader) #return in JSON format

     else:
        #if data is in str format
        if isinstance(data, str):
            data = json.loads(data)#json.loads() to convert string to JSON
        return data


def extract_calculate(data_list):
    extracted = [] #empty list to store extracted data
    for record in data_list:
        try:
            if not isinstance(record,dict):
                 logging.error(("Record is not a dictionary: %s",record) + "line number:"+str(e.__traceback__.tb_lineno))
            SID = record.get('SID') or record.get('sid') or record.get('student_id') or record.get('Student_ID')
            if not SID:
                raise ValueError("Student ID not found")
            English = float(record.get('English') or record.get('english')or 0)
            Math = float(record.get('Math') or record.get('math') or 0)
            Physics = float(record.get('Physics') or record.get('physics') or record.get('Phy') or record.get('phy') or 0)
            Chemistry = float(record.get('Chemistry') or record.get('chemistry') or record.get('Chem') or record.get('chem') or 0)
            Biology = float(record.get('Biology') or record.get('biology') or record.get('Bio') or record.get('bio') or 0)
            Total = English + Math + Physics + Chemistry + Biology
            Percentage = (Total / 500) * 100

            extracted.append((SID, English, Math, Physics, Chemistry, Biology, Total, Percentage))
        except Exception as e:
            logging.error(("Error processing record: %s", e) + "line number:"+str(e.__traceback__.tb_lineno))
            continue


    return extracted
    
# def read_input():
#     """ Reads if data input is in CSV or raw JSON format."""





    

    