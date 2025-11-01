import csv
import matplotlib.pyplot as plt


def calculate():
    matches_file = open('./data/matches.csv','r')
    matches_reader = csv.DictReader(matches_file)

    match_id_2015 = set()

    for match_info in matches_reader:
        if match_info['season'] == '2015':
            match_id_2015.add(match_info['id'])


    matches_file.close()

    runs_given = {}
    no_of_balls = {}

    del_file = open('./data/deliveries.csv')
    del_reader = csv.DictReader(del_file)

    for del_info in del_reader:
        if del_info['match_id'] in match_id_2015:
            bowler_name = del_info['bowler']
            total_runs = int(del_info['total_runs'])
            bye_runs = int(del_info['bye_runs'])
            legbye_runs = int(del_info['legbye_runs'])

            if not bye_runs and not legbye_runs:
                runs_given[bowler_name] = runs_given.get(bowler_name,0) + total_runs

            wide_ball = int(del_info['wide_runs'])
            noball = int(del_info['noball_runs'])

            if not wide_ball and not noball:
                no_of_balls[bowler_name] = no_of_balls.get(bowler_name,0) + 1

    del_file.close()


    bowlers_economy = list()

    for bowler in runs_given:
        if bowler not in no_of_balls:
            continue

        if no_of_balls[bowler] == 0:
            continue
        
        overs = no_of_balls[bowler] / 6
        runs = runs_given[bowler]

        economy = runs / overs

        bowlers_economy.append((economy,bowler))

    top_bowlers = sorted(bowlers_economy)

    return top_bowlers[:10]

def plot(data):
    bowlers = [bowler for _, bowler in data]
    economies = [eco for eco, _ in data]

    plt.figure(figsize=(10,6))
    plt.bar(bowlers, economies, color='skyblue')
    plt.xlabel("Bowler")
    plt.ylabel("Economy Rate")
    plt.title("Top 10 Economical Bowlers in IPL 2015")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.savefig('./outputs/top_10_economical_bowlers_2015.png')
    plt.close()

def execute():
    data = calculate()
    plot(data)

if __name__ == "__main__":
    execute()



