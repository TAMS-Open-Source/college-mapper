import pandas as pd
from .state_abbrev import US_STATE_ABBREV

data_link = './data/college_information.csv'
if __name__ == '__main__':
  data_link = '../data/college_information.csv'

NAME_IND = 'institution name'
ENROLLMENT_IND = 'DRVEF122019.12-month full-time equivalent enrollment: 2018-19'
CITY_IND = 'HD2019.City location of institution'
STATE_IND = 'HD2019.FIPS state code'

def getCollegeByID(college_id, toJSON = False):
  '''
  Returns college dict of information (full, with everything) based on id.
  Assumes id is given as an integer.
  '''


  data = pd.read_csv(data_link)

  # check id against all college ids
  for key, unit_id in data['unitid'].items():
    if college_id == unit_id:
      series = data[key:key+1].squeeze()
      if toJSON:
        return series.to_json()
      else:
        return series.to_dict()

  # if we reach here, nothing has been found from the data
  print("Nothing found")
  return None

def getShortCollegeByID(college_id):
  college_dict = getCollegeByID(college_id)
  if college_dict is None:
    return None
  new_dict = {
    'unitid': int(college_dict['unitid']),
    NAME_IND: college_dict[NAME_IND],
    ENROLLMENT_IND: college_dict[ENROLLMENT_IND],
    'city_and_state': f'{college_dict[CITY_IND]}, {US_STATE_ABBREV[college_dict[STATE_IND]]}'
  }
  return new_dict

# testing
if __name__ == '__main__':
  test_id = 100654
  print(getCollegeByID(test_id))