# The purpose of this file is primarily to serve as a base for the API
# Most functionality should be represented in src/

from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api, reqparse # reqparse allows for optional args
import pandas as pd
import json

from src.college_retrieval import getCollegeByID

app = Flask(__name__)
api = Api(app)

class College(Resource):
  def get(self):
    args = request.args
    college_id = args['id']

    college_id = int(college_id) # force the id to convert to int
    print(f'Got id as {college_id}')

    collegeDict = getCollegeByID(college_id, toJSON=True)
    # return error if no college is found
    if collegeDict is None:
      return { 'message': f'College with id {college_id} not found.' }, 404

    print(collegeDict)
    return { 'data' : collegeDict }, 200 # return data and 200 (success) code

api.add_resource(College, '/college')


from src.location import getTopCollegeDictsInBox

class CollegesInBox(Resource):

  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('swLat', type = float)
    self.reqparse.add_argument('swLon', type = float)
    self.reqparse.add_argument('neLat', type = float)
    self.reqparse.add_argument('neLon', type = float)
    self.reqparse.add_argument('num', type = int, default = 10)

  def get(self):
    args = self.reqparse.parse_args()
    swLat = args['swLat']
    swLon = args['swLon']
    neLat = args['neLat']
    neLon = args['neLon']
    num = args['num']

    if (not swLat or not swLon or not neLat or not neLon):
      return { 'message': 'At least one coordinate not provided.' }, 404


    college_list = getTopCollegeDictsInBox(swLat, swLon, neLat, neLon, num)

    return { 'data': college_list }, 200

api.add_resource(CollegesInBox, '/colleges_in_box')

from src.college_retrieval import getShortCollegeByID

class ShortCollege(Resource):
  def get(self):
    college_id = int(request.args['id'])
    short_dict = getShortCollegeByID(college_id)
    if not short_dict:
      return { 'message': f'No college found with id {college_id}' }, 404
    
    return { 'data': short_dict }, 200

api.add_resource(ShortCollege, '/short_college')

if __name__ == '__main__':
  # run flask app on localhost:5000
  app.run(host='localhost', port = 5000) # run our flask app