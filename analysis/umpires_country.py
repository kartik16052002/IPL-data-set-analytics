import csv
import matplotlib.pyplot as plt

def calculate():
    umpires_file = open('./data/umpires_country.csv','r')
    umpires_reader = csv.DictReader(umpires_file)

    no_of_umpires = {} # key - country

    for umpire_info in umpires_reader:
        if umpire_info['Country'] != 'India':
            no_of_umpires[umpire_info['Country']] = no_of_umpires.get(umpire_info['Country'],0) + 1
    

    umpires_file.close()

    return no_of_umpires

def plot(data):
    country = data.keys()
    no_of_umpires = data.values()

    plt.plot(country,no_of_umpires)
    plt.xlabel('Country')
    plt.ylabel("No of Umpires")
    plt.title('No of umpires by country in IPL')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('./outputs/umpires_country.png')
    plt.close()

def execute():
    data = calculate()
    plot(data)

if __name__ == "__main__":
    execute()