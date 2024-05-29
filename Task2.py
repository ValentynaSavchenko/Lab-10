#2.	Припустімо, у вас є рюкзак і набір предметів із певними вагами та вартостями. 
#Вам потрібно заповнити рюкзак таким чином, щоб максимізувати вартість обраних предметів, не перевищуючи місткість рюкзака.
#Автор Савченко Валентина 31І

def knapsack_greedy(items, max_weight):

  sorted_items = sorted(items, key=lambda item: item["value"] / item["weight"], reverse=True)

  selected_items = []
  current_weight = 0
  for item in sorted_items:
    if item["weight"] <= max_weight - current_weight:
      selected_items.append(item)
      current_weight += item["weight"]

  max_value = 0
  for item in selected_items:
    max_value += item["value"]

  return {
    "max_value": max_value,
    "selected_items": selected_items
  }

items = [
  {"weight": 6, "value": 3},
  {"weight": 3, "value": 4},
  {"weight": 1, "value": 5},
  {"weight": 5, "value": 6},
]

max_weight = 10

solution = knapsack_greedy(items, max_weight)

print(f"Максимальна сумарна вартість: {solution['max_value']}")
print(f"Обрані предмети:", solution["selected_items"])
