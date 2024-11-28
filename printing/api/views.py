from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Import printing related functions, classes
from printing.api.Functions.verify import *
from printing.api.Functions.CRUD import *
from printing.api.Functions.response import *
from printing.api.Functions.printerAPI import *
from printing.api.serializers import *
from account.api.serializers import *

# Print document view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PrintDocument(request):
    try:
        error = []
        
        # Check if print info
        VerifyPrintInfo(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Schedule print document
        Print(request)
        
        # Add new print info into database
        CreateNewPrintHistory(request)
        
        # Response
        return ResponseSuccessful("Document is being printed!")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
def ViewParameters(request):
    try:
        error = []

        # Check if there is an error
        if error:
            raise Exception()

        # Response
        return ResponseSuccessful()
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
def EditParameters(request):
    try:
        error = []
        
        # Check new parameters
        VerifyNewParameters(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Response
        return ResponseSuccessful("Parameters are being adjusted!")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)

@api_view(['GET'])
@permission_classes([IsAuthenticated])   
def ViewStudent(request):
    try:
        user_roles = request.user.groups.values_list('name', flat=True)
        if not ('admin' in user_roles or 'SPSO' in user_roles):
            return ResponseUnauthorized()
        errors = []
        VerifyStudentInfo(request, errors)
        if errors:
            return ResponseError(errors)

        filters = ast.literal_eval(request.body.decode("UTF-8"))
        name = filters.get('name')
        student_id = filters.get('student_id')

        students = UserAccount.objects.all()
        if name:
            students = students.filter(name__icontains=name)
        if student_id:
            students = students.filter(student_id=student_id)
        if not students.exists():
                return ResponseNotFound("Student not found.")
        account_ids = students.values_list('id', flat=True)
        return account_ids
    except Exception as e:
        return ResponseError([str(e)] if str(e) else ["Unexpected error occurred."])


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewHistoryRecord(request):
    try:
        user_roles = request.user.groups.values_list('name', flat=True)
        errors = []

        if 'admin' in user_roles or 'SPSO' in user_roles:
            VerifyHistoryRecord(request, errors)
            if errors:
                return ResponseError(errors)

            filters = ast.literal_eval(request.body.decode("UTF-8"))
            account_id = ViewStudent(request)
            records = ViewAllHistoryRecord(request).filter(account_id=account_id)

            if 'start_date' in filters and 'end_date' in filters:
                records = records.filter(
                    date__range=(
                        datetime.strptime(filters['start_date'], "%d-%m-%Y"),
                        datetime.strptime(filters['end_date'], "%d-%m-%Y")
                    )
                )
            if 'printer' in filters:
                records = records.filter(printer=filters['printer'])

            if not records.exists():
                return ResponseNotFound("No matching history records found.")

            serializer = HistorySerializer(records, many=True)
            return ResponseSuccessful(serializer.data, status_code=200)

        elif 'User' in user_roles:
            records = ViewAllHistoryRecord(request).filter(user=request.user)
            if not records.exists():
                return ResponseNotFound("No history records found.")

            serializer = HistorySerializer(records, many=True)
            return ResponseSuccessful(serializer.data, status_code=200)

        else:
            return ResponseUnauthorized()
    except Exception as e:
        return ResponseError([str(e)] if str(e) else ["Unexpected error occurred."])
