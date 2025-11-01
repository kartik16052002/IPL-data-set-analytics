import csv

matches_file = open('./data/matches.csv','r')
matches_reader = csv.DictReader(matches_file)

umpires = set()

for info in matches_reader:
    umpires.add(info['umpire1'])
    umpires.add(info['umpire2'])
    umpires.add(info['umpire3'])

matches_file.close()

umpires_list = open('./data/umpires.txt','w')

for umpire in umpires:
    umpires_list.write(umpire)
    umpires_list.write('\n')

umpires_list.close()