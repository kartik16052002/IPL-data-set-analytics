"""Moudule for reading comma seperated values"""
import csv

import matplotlib.pyplot as plt



def calculate():
    """Grand total of all the runs scored by each team in IPL"""

    matches_file = open('./data/deliveries.csv','r')
    matches_reader = csv.DictReader(matches_file)

    total_score = {} # grand total of all the score of each team in in IPL

    for match_info in matches_reader:
        batting_team = match_info['batting_team']
        if batting_team == 'Rising Pune Supergiant':
            batting_team = 'Rising Pune Supergiants'

        team_score = int(match_info['total_runs'])

        total_score[batting_team] = total_score.get(batting_team,0) + team_score


    matches_file.close()

    return total_score

def plot(data):
    """Plotting the data using matplotlib."""
    sorted_data = sorted(data.items(),key = lambda x : x[1],reverse=True)
    teams = [x[0] for x in sorted_data]
    scores = [x[1] for x in sorted_data]

    plt.figure(figsize=(10, 6))  # Add figure size to avoid crowding
    plt.plot(teams, scores, marker='o')

    plt.title("Total Runs Scored by Each IPL Team")
    plt.xlabel("Teams")
    plt.ylabel("Total Runs")

    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
    plt.tight_layout()  # Adjust layout to prevent cutting off labels

    plt.savefig('outputs/total_runs_by_team_img.png')
    


def execute():
    total_score_teamwise = calculate()
    plot(total_score_teamwise)


if __name__ == "__main__":
    execute()




