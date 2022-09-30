data = [
    {"name": "Algebra", "credits": 2},
    {"name": "EDA", "credits": 2},
    {"name": "Networks", "credits": 2},
    # {"name": "Calculus", "credits": 2},
    # {"name": "Databases", "credits": 2},
    # {"name": "Physic", "credits": 2},
    # # {
    #     "name": "Algebra",
    #     "credits": 2
    # },
    # {
    #     "name": "Algebra",
    #     "credits": 2
    # }
]


def recursive(data, index, used_credits, path, min_credits, max_credits, memo, key):
    path = path.copy()
    if index == len(data):
        return None

    currentData = data[index]
    currentCredits = currentData["credits"]
    used_credits += currentCredits

    if used_credits > max_credits:
        return None

    if used_credits < min_credits and index == len(data):
        return None

    if index >= len(data):
        return path

    path.append(currentData)

    
    key += currentData["name"] + "-"
    remainders = len(data) - index
    for j in range(1, remainders + 1):
        memo.append(
            recursive(
                data,
                index + j,
                used_credits,
                path,
                min_credits,
                max_credits,
                memo,
                key,
            )
        )

    if used_credits >= min_credits and used_credits <= max_credits:
        return path


memo = []
recursive(data, 0, 0, [], 4, 7, memo, "")

print(memo)
# print(list(filter(lambda x: x is not None, memo)))
