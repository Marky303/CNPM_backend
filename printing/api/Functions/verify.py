import json
import re
import os

from printing.models import *

def VerifyPrintInfo(request, error):
    # Get print info from reques
    dict = request.body.decode("UTF-8")
    info = json.loads(dict)
    
    # Get file type
    fileType = os.path.splitext(info['FileName'])[1][1:]
    
    # Get allowed files
    allowedFilesString = Setting.objects.get(id=1).AllowedFiles
    allowedFiles = [word.strip() for word in allowedFilesString.split(',')]

    if fileType not in allowedFiles:
        error.append("File không được hỗ trợ")
        
    # Check token
    # Get cost
    pageMultiplier = 1
    if info['Size'] == 'A3':
        pageMultiplier = 2
    if info['Size'] == 'A3':
        pageMultiplier = 4
    cost = pageMultiplier * int(info['Pages']) * int(info['Copies'])
    
    # Get current user token
    userToken = request.user.token
    
    if userToken < cost:
        error.append("Không đủ token")

    
    
def VerifySettings(request, error):
    # Get print info from reques
    dict = request.body.decode("UTF-8")
    info = json.loads(dict)
    
    # Check if file string is formatable
    pattern = r'^(\w+)(,\s*\w+)*$'
    if not re.fullmatch(pattern, info['AllowedFiles']):
        error.append("Sai định dạng")