import itertools, random

print('{0:^30}'.format('K O C O K   K A R T U'))
print('='*30)

kartu = list(itertools.product(range(1,14),['Keriting','Hati','Wajik','Waru']))
random.shuffle(kartu)

print('{0:^30}'.format('hasil'))
print('')

for i in range(5):
   print(kartu[i][0], 'of', kartu[i][1])