
import csv
import matplotlib.pyplot as plt

def calculate():
    matches_id = set()
    matches_file = open('./data/matches.csv','r')
    matches_reader = csv.DictReader(matches_file)

    for match_info in matches_reader:
        if match_info['season'] == '2016':
            matches_id.add(match_info['id'])

    matches_file.close()

    extra_runs_by_team = {}
    # key => bowling_team
    # val => exta runs

    deliveries_file = open('./data/deliveries.csv')
    deliveries_reader = csv.DictReader(deliveries_file)

    for del_info in deliveries_reader:
        if del_info['match_id'] in matches_id:
            extra_runs = int(del_info['extra_runs'])
            bowling_team = del_info['bowling_team']

            extra_runs_by_team[bowling_team] = extra_runs_by_team.get(bowling_team,0) + extra_runs

    return extra_runs_by_team



def plot(data):
    if not data:
        print("No data to plot.")
        return

    teams = list(data.keys())
    extra_runs = list(data.values())

    plt.figure(figsize=(12, 6))
    plt.bar(teams, extra_runs, color='skyblue', edgecolor='black')

    plt.xlabel("Teams")
    plt.ylabel("Extra Runs Conceded")
    plt.title("Extra Runs Conceded per Team in IPL 2016")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.savefig('./outputs/extra_runs_2016.png')
    plt.close()

def execute():
    data = calculate()
    plot(data)

if __name__ == "__main__":
    execute()
