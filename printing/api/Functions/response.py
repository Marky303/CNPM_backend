from rest_framework.response import Response
from rest_framework import status


# Response if the action was successsful
def ResponseSuccessful(content, status=status.HTTP_200_OK):
    content = {'detail': content}
    return Response(content, status=status)

# Reponse the analysis result object for rendering
def ResponseObject(content, status=status.HTTP_200_OK):
    return Response(content, status=status)

# Response if the action incurred error
def ResponseError(error=["Something happened"]):
    content = {'error': error}
    return Response(content, status=status.HTTP_400_BAD_REQUEST)    