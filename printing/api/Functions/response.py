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