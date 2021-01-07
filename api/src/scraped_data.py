import wikipedia
import pandas as pd

data = pd.read_csv('../data/new_college_information.csv')

CITY_IND = 'HD2019.City location of institution'
STATE_IND = 'HD2019.FIPS state code'

def getWikipediaDescription(name):
  description = ""
  try:
    description = wikipedia.summary(name)
    print("Description success.")
    print(description)
  except:
    description = "Couldn't get description"
    print("No Description Found.")
  return description

def addDescriptionsToData(num = len(data)):
  descriptions = []
  counter = 0
  for key, name in data['institution name'].items():
    summary = getWikipediaDescription(name)
    descriptions.append(summary)

    counter += 1
    if (counter == num):
      while len(descriptions) < len(data):
        descriptions.append('Nothing added.')
      break

  data["description"] = descriptions
  data.to_csv('new_college_information.csv', index=False)
  return

def getWikipediaURL(name):
  url = ""
  try:
    city = wikipedia.page(name)
    url = city.url
    print(f'Found link for {name}:\n {url}')
  except:
    print(f'Could not find city link for {name}')
    pass
  return url

def addCityURLsToData(num = len(data)):
  urls = []
  counter = 0
  for index, row in data.iterrows():
    city_name = row[CITY_IND]
    state_name = row[STATE_IND]
    url = getWikipediaURL(f'{city_name} {state_name}')
    urls.append(url)
    # give live recording of progress finding the wikipedia urls
    print(f'Progress: {round((counter / num) * 100, 1)}%')

    counter += 1
    if (counter == num):
      while len(urls) < len(data):
        urls.append("")
      break

  data["city_url"] = urls
  data.to_csv('../data/temp_information.csv', index=False)
  return 

if __name__ == '__main__':
  addCityURLsToData()
