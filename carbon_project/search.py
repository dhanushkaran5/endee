import csv

def hybrid_search(query):
    results = []
    query = str(query).lower()

    with open("dataset.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if (query in row["name"].lower() or
                query in row["co2"] or
                query in row["price"]):
                results.append(row)

    return results
