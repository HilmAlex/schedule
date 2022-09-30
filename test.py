data = [
    {
        "name": "Algebra",
        "code": "1SW",
        "group": "1",
        "credits": 3,
        "schedule": {
            "Monday": {
                "init": "14:00",
                "end": "16:00"
            },
            "Wednesday": {
                "init": "16:00",
                "end": "18:00"
            },
            "Friday": {
                "init": "16:00",
                "end": "18:00"
            }
        }
    },

    {
        "name": "EDA",
        "code": "1SW",
        "group": "1",
        "credits": 3,
        "schedule": {
            "Monday": {
                "init": "01:00",
                "end": "02:00"
            },
            "Wednesday": {
                "init": "01:00",
                "end": "02:00"
            },
            "Thursday": {
                "init": "01:00",
                "end": "02:00"
            }
        }
    },

    {
        "name": "Networks",
        "code": "1SW",
        "group": "1",
        "credits": 3,
        "schedule": {
            "Monday": {
                "init": "11:00",
                "end": "13:00"
            },
            "Wednesday": {
                "init": "07:00",
                "end": "09:00"
            },
            "Friday": {
                "init": "11:00",
                "end": "13:00"
            }
        }
    }
]

hours_in_schedule = [
    {"Monday": ["13:00"]},
    {"Tuesday": ["13:00"]},
    {"Wednesday": ["13:00"]},
    {"Thursday": ["13:00"]},
    {"Friday": ["13:00"]},
    {"Saturday": ["13:00"]}
]

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# cant be only by credits because they need to be restarted
# we need another variable for base case i think it should be the clash of schedules that is matching
# the schedule of each element of the dictionary with a type of list where we save the hours chosen


def create_subject_schedule(data, credits, hours_in_schedule, sub_idx, days_of_week, path, subjects_in_schedule, memo):

    if sub_idx > 2:
        return path

    for day in days_of_week:
        if day in data[sub_idx]["schedule"]:
            if credits == 9 or data[sub_idx]["schedule"][day]["init"] in hours_in_schedule[days_of_week.index(day)][day]:
                return path

    if credits > 9:
        return path
    
    else:
        subjects_in_schedule = data[sub_idx]["name"] 
        path.append(subjects_in_schedule)
        memo.append(subjects_in_schedule)
        if sub_idx < 2:
            subjects_in_schedule = data[sub_idx + 1]["name"]    
        for day in days_of_week:
            if day in data[sub_idx]["schedule"]:
                hours_in_schedule[days_of_week.index(day)][day].append(data[sub_idx]["schedule"][day]["init"])
        return create_subject_schedule(data, credits + data[sub_idx]["credits"], hours_in_schedule, sub_idx + 1, days_of_week, path, subjects_in_schedule, memo)

def main():
    pass #used to call create_subject_schedule and restart variables for other schedules

print(create_subject_schedule(data, 0, hours_in_schedule, 0, days_of_week, [], "", []))


