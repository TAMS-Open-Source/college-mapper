import pandas as pd
import math

DATA_LOC = './data/college_information.csv'
if __name__ == '__main__':
  DATA_LOC = '../data/college_information.csv'

LAT_IND = 'HD2019.Latitude location of institution'
LON_IND = 'HD2019.Longitude location of institution'
MATH_SAT_IND = 'ADM2019.SAT Math 75th percentile score'
ENG_SAT_IND = 'ADM2019.SAT Evidence-Based Reading and Writing 75th percentile score'

colleges = pd.read_csv(DATA_LOC)

# Bounding box coordinates typically expressed in terms of 
# Southwestern and Northeastern coordinates, with the rest
# logically inferred.

# take southwestern latitude, southwestern longitude,
# northeastern latitude, and northeastern longitude!

# we can probably make a wrapper to use objects or something, but
# for now we'll be taking things in individually (as in, the latter
# four are bounding coordinates)
# (Assumes inputs are Numbers)
def collegeInBox(lat, lon, swLat, swLon, neLat, neLon):
  withinLatitudeRange = (lat >= swLat) and (lat <= neLat)
  withinLongitudeRange = (lon >= swLon) and (lon <= neLon)

  if withinLatitudeRange and withinLongitudeRange:
    return True
  else:
    return False

def getCollegesInBox(swLat, swLon, neLat, neLon):
  return_rows = []

  # iterate through each row in the dataframe
  for index, row in colleges.iterrows():
    college_lat = row[LAT_IND]
    college_lon = row[LON_IND]
    # check if each college is in the bounding box; if so, add a custom dict with 
    # relevant data to return to the web interface
    if collegeInBox(college_lat, college_lon, swLat, swLon, neLat, neLon):
      return_rows.append(row.to_dict())

  return return_rows

def convertRowsToDicts(rows):
  return_dicts = []
  for row in rows:
    college_lat = row[LAT_IND]
    college_lon = row[LON_IND]
    unitid = row['unitid']

    custom_dict = { 'unitid': unitid, 'lat': college_lat, 'lon': college_lon }
    return_dicts.append(custom_dict)
  return return_dicts

def getCollegeDictsInBox(swLat, swLon, neLat, neLon):
  return convertRowsToDicts(getCollegesInBox(swLat, swLon, neLat, neLon))

# returns colleges with highest composite SAT scores in the bounding box;
# by default, returns 10, but parameter can adjust this amount
def getTopCollegesInBox(swLat, swLon, neLat, neLon, num):
  college_list = getCollegesInBox(swLat, swLon, neLat, neLon)
  # take out colleges with no record of SAT score
  list_no_nans = []
  for college in college_list:
    if math.isnan(college[MATH_SAT_IND]) or math.isnan(college[ENG_SAT_IND]):
      # print('NaN found!')
      pass
    else:
      list_no_nans.append(college)

  # sort list with respect to both 
  sorted_list = sorted(list_no_nans, key=lambda dict: (dict[MATH_SAT_IND] + dict[ENG_SAT_IND])/2, reverse=True)
  # return first ten items
  short_list = sorted_list[:10]
  # printing to ensure validity of function
  # for college in short_list:
  #   print(college['institution name'])
  #   print(f'Math Score: {college[MATH_SAT_IND]}')
  return sorted_list[:num]

def getTopCollegeDictsInBox(swLat, swLon, neLat, neLon, num = 10):
  '''
  Returns the top
  '''
  return convertRowsToDicts(getTopCollegesInBox(swLat, swLon, neLat, neLon, num))

# testing grounds
if __name__ == '__main__':
  UNT_COORDS = { 'lat': 33.211178, 'lon': -97.148422 }
  HARVARD_COORDS = { 'lat': 42.374471, 'lon': -71.118313 } 
  print(getTopCollegeDictsInBox(UNT_COORDS['lat'], UNT_COORDS['lon'], HARVARD_COORDS['lat'], HARVARD_COORDS['lon']))
