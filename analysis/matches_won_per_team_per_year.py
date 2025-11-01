import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def calculate():
    starting_season = 2008
    total_season = 10
    matches_file = open('./data/matches.csv','r')
    matches_reader = csv.DictReader(matches_file)

    matches_won = defaultdict(lambda: [0]*total_season)
    # key - team name 
    # val = A list of no of matches won per year starting from 2008

    for match_info in matches_reader:
        if match_info['result'] == 'normal':
            winner_team = match_info['winner']
            match_year = int(match_info['season'])

            matches_won[winner_team][match_year - starting_season] += 1

    matches_file.close()

    return matches_won



def plot(data):
    if not data:
        print("No data to plot.")
        return

    starting_season = 2008
    num_seasons = 10
    years = [starting_season + i for i in range(num_seasons)]

    teams = list(data.keys())
    num_teams = len(teams)

    # Base x positions for each year
    x_indexes = list(range(num_seasons))
    cluster_width = 0.8
    bar_width = cluster_width / num_teams  # each team gets small width

    plt.figure(figsize=(14, 7))

    #  Shift each team horizontally to avoid overlap
    for i, team in enumerate(teams):
        x_positions = [x + i * bar_width for x in x_indexes]
        plt.bar(x_positions, data[team], width=bar_width, label=team)

    # Center x-axis labels under each cluster
    plt.xticks([x + cluster_width / 2 for x in x_indexes], years)

    plt.xlabel("Season")
    plt.ylabel("Matches Won")
    plt.title("Number of Matches Won per Team per Season (Grouped Bar Chart)")
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', fontsize='small')
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    plt.tight_layout()

    plt.savefig('outputs/grouped_matches_won_per_season.png')
    plt.close()


def execute():
    data = calculate()
    plot(data)


if __name__ == "__main__":
    execute()



