import pandas as pd

data_link = '../data/college_information.csv'
new_data_link = '../data/new_info.csv'

previous_information = pd.read_csv('../data/college_information.csv')
new_information = pd.read_csv('../data/new_info.csv')

ENROLLMENT_IND = 'DRVEF122019.12-month full-time equivalent enrollment: 2018-19'
WEB_IND = "HD2019.Institution's internet website address"
ADM_WEB_IND = 'HD2019.Admissions office web address'
FIN_AID_WEB_IND = 'HD2019.Financial aid office web address'
ONL_APP_WEB_IND = 'HD2019.Online application web address'

new_categories = [FIN_AID_WEB_IND, ONL_APP_WEB_IND]

def addNewCategories():
  for category in new_categories:
    new_list = new_information[category]
    if new_list.empty:
      print("Error finding category")
    previous_information[category] = new_list

  previous_information.to_csv('../data/temp_information.csv', index=False)

if __name__ == "__main__":
  addNewCategories()