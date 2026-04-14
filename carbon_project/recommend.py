import csv

def recommend_tree(budget, co2_goal):
    matched = []

    with open("dataset.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if int(row["price"]) <= budget and int(row["co2"]) >= co2_goal:
                matched.append(row)

    return matched
