def algorithm(string, dictionary, m):
  x = 0
  letters = {'0':0}
  name = string
  if m == 1:
      name = name[name.find('0') + 1:] + name[:name.find('0')]
      return name
  for let in name:
    if let == '0':
      letters['0'] += 1
  while letters['0'] > 0:
    if dictionary[x] - 1 == 0:
        name = name[name.find('0')+1:] + name[:name.find('0')]
        del dictionary[x]
        letters['0'] = letters['0'] - 1
        x = (x+1)%m
        
    else:
        dictionary[x] = dictionary[x] - 1
        name = name[name.find('0') + 1:] + name[:name.find('0') + 1]
    
  return name
#Main Program

start = input().split()
sentence = input()
cheer = input().split()

o_num = {}

for z in range(int(start[1])):
  o_num[z] = int(cheer[z])

print(algorithm(sentence, o_num, int(start[1])))