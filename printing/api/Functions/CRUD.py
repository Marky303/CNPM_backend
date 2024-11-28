import ast
from datetime import datetime
import random
import string
from decimal import Decimal

# Import models
from printing.models import *
from account.models import *

def CreateNewPrintHistory(request):
    pass

def ViewAllStudent(request):
    students = UserAccount.object.all()
    return students

def ViewAllHistoryRecord(request):
    records = History.objects.all()
    return records
