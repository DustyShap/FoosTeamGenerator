#Two person Tourny Random generator

import random


people =[]

while True:
        name = input('Please enter a participant.Enter done to finish: ')
        people.append(name)
        if name == 'done':
                people.remove('done')
                if (len(people)%2) != 0:
                        print('Odd number of players! Add more please')
                else:
                        break
                
        elif len(name) == 0:
                print('')
                print('Input was blank')
                people.pop()

print('')
print('You have entered a total of %d players' % (len(people)))
       
pairs = {}
for p in range(len(people) // 2):
	pairs[p+1] = (people.pop(random.randrange(len(people))),
		      people.pop(random.randrange(len(people))))

for k in pairs:
        print("Team %d: %s and %s" % (k, pairs[k][0], pairs[k][1]))
