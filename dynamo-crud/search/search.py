import logging
import boto3
import json
import uuid
from functools import reduce
from boto3.dynamodb.conditions import Key, And

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.client('dynamodb')

def search(event, context):
    """
    This function will perform a search against dynamodb.
    """

    data = json.loads(event['body'])
    # define the fields to filter by
    field_list = ['make','model','submodel','year','engine_make','engine_family','engine_code']
    # create an empty filter dict
    filters = {}
    # loop through filter fields and search for item in data
    # if exists, assign to filter dict
    for field in field_list:
        if field in data:
            filters.update({field,data[field]})
    # get the table to search
    table = dynamodb.Table('Vehicle')
    # apply the filters to the search
    items = table.scan(FilterExpression=reduce(And, ([Key(k).eq(v) for k, v in filters.items()])))
    # return the items in the response
    response = {
        'statusCode': 200,
        'items':json.dumps(items['Items']),
    }
    
    return response