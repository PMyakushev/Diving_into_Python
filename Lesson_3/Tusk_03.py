from typing import Dict, List, Tuple

def knapsack(items: Dict[str, float], maximum_weight: float) -> List[str]:
    # Преобразуем словарь в список
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0] * (int(maximum_weight) + 1) for _ in range(n + 1)]

    # Заполнение таблицы динамического программирования
    for i in range(1, n + 1):
        item, weight = item_list[i - 1]
        for w in range(int(maximum_weight) + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - int(weight)] + int(weight))
            else:
                dp[i][w] = dp[i - 1][w]

    # Нахождение выбранных вещей
    result = []
    w = int(maximum_weight)
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, weight = item_list[i - 1]
            result.append(item)
            w -= int(weight)

    return result

# Пример использования
gear = {
    "tent": 2.5,
    "sleeping bag": 1.0,
    "food": 1.5,
    "water": 3.0,
    "first aid kit": 0.5,
    "clothes": 2.0,
    "flashlight": 0.5,
}

max_capacity = 5.0
selected_gear = knapsack(gear, max_capacity)
print("Вещи, которые можно взять в поход:", selected_gear)
