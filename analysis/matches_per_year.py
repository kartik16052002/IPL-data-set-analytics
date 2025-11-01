import csv
import matplotlib.pyplot as plt

def calculate():
    matches_file = open('./data/matches.csv','r')

    matches_reader =  csv.DictReader(matches_file)

    matches_by_year = {}

    for match_info in matches_reader:
        match_year = int(match_info['season'])
        matches_by_year[match_year] = matches_by_year.get(match_year,0) + 1

    matches_file.close()

    return matches_by_year

def plot(data):
    match_year = sorted(data.keys())
    no_of_matches = [data[key] for key in data]

    plt.bar(match_year,no_of_matches)
    plt.title('No of matches in IPL per year')
    plt.xlabel('Year')
    plt.ylabel('Matches Played')

    plt.savefig('./outputs/matches_played_yearwise.png')
    plt.close()

def execute():
    no_of_matches_per_year = calculate()
    plot(no_of_matches_per_year)

if __name__ == "__main__":
    execute()

