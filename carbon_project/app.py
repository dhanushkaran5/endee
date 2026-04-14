from search import hybrid_search
from recommend import recommend_tree

print("🌳 Tree Plantation System\n")

query = input("Enter search (name/co2/price): ")
print("\nSearch Results:")
print(hybrid_search(query))

budget = int(input("\nEnter your budget: "))
goal = int(input("Enter CO2 goal: "))

print("\nRecommended Trees:")
print(recommend_tree(budget, goal))
