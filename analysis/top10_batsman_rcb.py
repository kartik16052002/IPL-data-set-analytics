import csv
import matplotlib.pyplot as plt

def calculate():
    matches_file = open('./data/deliveries.csv','r')
    matches_reader = csv.DictReader(matches_file)

    batsman_scores_all_matches = {}

    for match_info in matches_reader:
        if match_info['batting_team'] == 'Royal Challengers Bangalore':
            batsman = match_info['batsman']
            batsman_runs = int(match_info['batsman_runs'])

            batsman_scores_all_matches[batsman] = batsman_scores_all_matches.get(batsman,0) + batsman_runs


    matches_file.close()

    sorted_scores = sorted(batsman_scores_all_matches.items(), key = lambda x : x[1], reverse = True)

    return sorted_scores[:10]

def plot(data):
    player = [x[0] for x in data]
    scores = [x[1] for x in data]

    plt.figure(figsize=(10, 6))  # Add figure size to avoid crowding
    plt.plot(player, scores, marker='o')

    plt.title("Top 10 batsman of RCB")
    plt.xlabel("Players")
    plt.ylabel("Total Runs")

    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
    plt.tight_layout()  # Adjust layout to prevent cutting off labels

    plt.savefig('outputs/total_scorers_rcb.png')

def execute():
    scores = calculate()
    plot(scores)

if __name__ == "__main__":
    execute()

