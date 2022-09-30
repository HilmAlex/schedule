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


def solve():
    data = [
        {"name": "Algebra", "credits": 3},
        {"name": "EDA I", "credits": 3},
        {"name": "Networks", "credits": 4},
        {"name": "Calculus", "credits": 3},
        {"name": "Databases", "credits": 3},
        {"name": "Physic", "credits": 3},
        {"name": "EDA II", "credits": 3},
        {"name": "Programming", "credits": 3},
        {"name": "Mathematics", "credits": 3},
    ]

    min_credits = 9
    max_credits = 15

    memo = []

    for i in range(0, len(data)):
        recursive(data, i, 0, [], min_credits, max_credits, memo, "")

    print(list(filter(lambda x: x is not None, memo)))

solve()