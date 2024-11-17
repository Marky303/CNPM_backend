import ast

def VerifyPrintInfo(request, error):
    # Get print info from reques
    dict = request.body.decode("UTF-8")
    printInfo = ast.literal_eval(dict)
    
    # Check if print info is valid
    if not printInfo['FileType'] == '.pdf':
        error.append("File type is not valid")
def VerifySPSOinfo(request, error):
    user_roles = request.user.groups.values_list('name', flat=True)
    if 'admin' not in user_roles:
        error["message"] = "Bạn không có quyền truy cập thông tin máy in. Chỉ admin mới được phép."
        return False
    return True