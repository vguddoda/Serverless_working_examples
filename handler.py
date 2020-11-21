import json
import os

def hello(event, context):
   
    print ("hi Updated second time!")
    print (os.environ['FIRST_NAME'])
    print (os.environ['LAST_NAME'])
    return "hello-world"

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
