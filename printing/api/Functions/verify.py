import ast

def VerifyPrintInfo(request, error):
    # Get print info from reques
    dict = request.body.decode("UTF-8")
    printInfo = ast.literal_eval(dict)
    
    # Check if print info is valid
    if not printInfo['FileType'] == '.pdf':
        error.append("File type is not valid")