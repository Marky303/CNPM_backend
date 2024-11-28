import datetime
import ast
import re

def VerifyPrintInfo(request, error):
    # Get print info from reques
    dict = request.body.decode("UTF-8")
    printInfo = ast.literal_eval(dict)
    
    # Check if print info is valid
    if not printInfo['FileType'] == '.pdf':
        error.append("File type is not valid")

def VerifyStudentInfo(request, error):
    dict = request.body.decode("UTF-8")
    filter = ast.literal_eval(dict)
    name = filter.get('name')
    student_id = filter.get('student_id')
    if name and not re.match(r'^[a-zA-Z\s]{2,}$', name):
        error.append("Invalid name")
    if student_id and not re.match(r'^\d{8}$', student_id):
        error.append("Invalid id")
    
def VerifyHistoryRecord(request, error):
    dict = request.body.decode("UTF-8")
    filters = ast.literal_eval(dict)
    start_date = filters.get('start_date')
    end_date = filters.get('end_date')

    if start_date:
        try:
            datetime.strptime(start_date, "%d-%m-%Y")
        except ValueError:
            error.append("Invalid start date format. Expected format: DD-MM-YYYY.")
    
    if end_date:
        try:
            datetime.strptime(end_date, "%d-%m-%Y")
        except ValueError:
            error.append("Invalid end date format. Expected format: DD-MM-YYYY.")

    if start_date and end_date:
        if datetime.strptime(start_date, "%d-%m-%Y") > datetime.strptime(end_date, "%d-%m-%Y"):
            error.append("End date cannot be earlier than start date.")

    printer_filter = filters.get('printer')
    if printer_filter:
        if not isinstance(printer_filter, str):
            error.append("Invalid printer filter.")
