from rest_framework.response import Response
from rest_framework import status


# Response if the action was successsful
def ResponseSuccessful(content, status=status.HTTP_202_ACCEPTED):
    content = {'detail': content}
    return Response(content, status=status)


# Response if the action incurred error
def ResponseError(error=["Something happened"]):
    content = {'error': error}
    return Response(content, status=status.HTTP_400_BAD_REQUEST)    

def ResponseNotFound(error=["Not found"]):
    content = {'error': error}
    return Response(content, status=status.HTTP_404_NOT_FOUND)   


def ResponseUnauthorized(error=["Unauthorized"]):
    content = {'error': error}
    return Response(content, status=status.HTTP_403_FORBIDDEN)   
