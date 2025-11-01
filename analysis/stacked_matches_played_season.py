import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def calculate():
    num_seasons = 10
    starting_season = 2008
    matches_played_per_year = defaultdict(lambda: [0]*num_seasons)

    matches_file = open('./data/matches.csv','r')
    matches_reader = csv.DictReader(matches_file)


    for match_info in matches_reader:
        season = int(match_info['season'])
        team1 = match_info['team1']
        team2 = match_info['team2']

        matches_played_per_year[team1][season - starting_season] += 1
        matches_played_per_year[team2][season - starting_season] += 1

    matches_file.close()
    
    return matches_played_per_year

def plot(data):
    num_season = 10
    teams = list(data.keys())
    seasons = list(range(2008, 2008 + num_season))
    num_teams = len(teams)
    bar_width = 0.8 / num_teams  # adjust based on number of teams

    plt.figure(figsize=(12, 6))

    for idx, team in enumerate(teams):
        x_positions = [year + idx * bar_width for year in range(len(seasons))]
        plt.bar(
            x_positions,
            data[team],
            width=bar_width,
            label=team
        )

    plt.xlabel('Season')
    plt.ylabel('Matches Played')
    plt.title('Matches Played per Team per Season')
    plt.xticks(
        [i + 0.4 for i in range(len(seasons))],
        seasons
    )
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('outputs/matches_bar_chart.png')
    plt.close()




def execute():
    matches_played = calculate()
    plot(matches_played)


if __name__ == "__main__":
    execute()


