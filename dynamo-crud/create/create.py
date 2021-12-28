import logging
import boto3
import json
import uuid

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.client('dynamodb')

def create(event, context):

    data = json.loads(event['body'])
    field_list = ['make','model','submodel','year']
    if(all(x in data for x in field_list)):
        logging.error("Validation Failed")
        raise Exception("Couldn't create the vehicle")

    table = dynamodb.Table('Vehicle')

    item = {
        'id':str(uuid.uuid1()),
        'make':data['make'],
        'model':data['model'],
        'submodel':data['submodel'],
        'year':data['year'],
        'engine_make':data['engine_make'],
        'engine_family':data['engine_family'],
        'engine_code':data['engine_code']
    }

    table.put_item(Item=item)

    response = {
        'statusCode': 201,
        'body': 'successfully created vehicle!',
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    
    return response