import sys

## Converts phone numbers to all numeric digits

rawnums = [2,3,4,5,6,7,8,9]
rawletters = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
data = zip(rawletters, rawnums)
data_dict = dict(data)

phone_dict = {}
for key in data_dict.keys():
  for char in key:
    phone_dict[char] = data_dict[key] 
    #print char, data_dict[key]

def process(line):
  # Process each line of input here
  outputlist = []
  for char in list(line.strip()):
    try: 
       int(char)
       outputlist.append(char)  
    except ValueError:
       outputlist.append(phone_dict[char.upper()])
  phonenumber = ''.join(str(x) for x in outputlist) 
  return phonenumber

lines = sys.stdin.readlines()

processed = map(process, lines)
for line in processed:
    print line.strip()

