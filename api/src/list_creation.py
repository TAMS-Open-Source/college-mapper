import pandas as pd

data_link = './data/college_information.csv'
colleges = pd.read_csv(data_link)

def sanitizeName(name):
  return name.replace('--', '-')

def getIDByCollegeName(name):
  name = sanitizeName(name)

  for index, row in colleges.iterrows():
    found_name = row['institution name']
    if found_name.lower() == name.lower():
      return row['unitid']
  return None

def manualCreation():
  id_arr = []

  usrInput = input('College: ')
  while usrInput != 'DONE':
    id = getIDByCollegeName(usrInput)
    if not id:
      print(f'Could not find college with name {usrInput}')
    else:
      print(f'Found id: {id}')
      id_arr.append(id)
    usrInput = input('College: ')

  print(id_arr)

def usNewsCreation(source, num = 50):
  college_arr = []
  file = open(source, 'r')
  counter = 0
  for line in file:
    line = line.lower()
    if 'university' in line or 'college' in line:
      college_arr.append(line.strip())
  college_ids = []
  for college_name in college_arr:
    id = getIDByCollegeName(college_name)
    while not id:
      print(f"Couldn't find id for {college_name}.")
      new_name = input("Correct name: ")
      id = getIDByCollegeName(new_name)
    college_ids.append(id)
  print(college_ids[:num])


def print50FromInput():
  usrInput = input("Give it here: ")
  usrInput = usrInput.replace('[', '')
  usrInput = usrInput.replace(']', '')
  id_arr = usrInput.split(', ')
  int_arr = [int(i) for i in id_arr]
  print(int_arr[:50])

def removeDuplicatesFromInput():
  usrInput = input("Give it here: ")
  usrInput = usrInput.replace('[', '')
  usrInput = usrInput.replace(']', '')
  id_arr = usrInput.split(', ')
  int_arr = [int(i) for i in id_arr]
  res = []
  # ensure nothing that gets added to res are duplicates
  for i in int_arr:
    if i not in res:
      res.append(i)
  print(f'Length of result: {len(res)}')
  print(res[:25])

if __name__ == "__main__":
  removeDuplicatesFromInput()
  