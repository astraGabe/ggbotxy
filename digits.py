def algorithm(string, dictionary, m):
  x = 0
  letters = {'0':0}
  name = string
  for let in name:
    if let == '0':
      letters['0'] += 1
  while letters['0'] > 0:
    if name[0] == '0':
      if m == 1:
        return name[1:]
      if dictionary[x] - 1 == 0:
        name = name[1:]
        letters['0'] = letters['0'] - 1
        del dictionary[x]
      else:
        name = name[1:] + name[0]
        dictionary[x] = dictionary[x] - 1
        x = (x+1)%m
    else:
      name = name[1:] + name[0]
  return name
#Main Program

start = input().split()
sentence = input()
cheer = input().split()

o_num = {}

for z in range(int(start[1])):
  o_num[z] = int(cheer[z])

print(algorithm(sentence, o_num, int(start[1])))