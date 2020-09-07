import time

projects_ids = {
    123: 1,
    456: 1,
    789: 1,
    1011: 1,
    1112: 1,
    1213: 1,
    1415: 1,
    1617: 1,
    1819: 1,
    2021: 1,
    2122: 1,
    2224: 1,
    2326: 1,
    2428: 1,
    2630: 1,
    2840: 1,
    3060: 1,
    3280: 1
}

projects = {
    "project1": {
        "id": 123
    },
    "proj2": {
        "id": 456
    },
    "someproject1": {
        "id": 789
    },
    "someproject2": {
        "id": 1011
    },
    "someproject3": {
        "id": 1112
    },
    "proj3": {
        "id": 1213
    },
    "someproject4": {
        "id": 1415
    },
    "someproject5": {
        "id": 1617
    },
    "someproject6": {
        "id": 1819
    },
    "project2": {
        "id": 2021
    },
    "someproject7": {
        "id": 2122
    },
    "project3": {
        "id": 2224
    },
    "someproject8": {
        "id": 2326
    },
    "project4": {
        "id": 2428
    },
    "project5": {
        "id": 2630
    },
    "someproject9": {
        "id": 2840
    },
    "proj4": {
        "id": 3060
    },
    "project6": {
        "id": 3280
    }
}

start1 = time.perf_counter()
result1 = list(filter(lambda p: projects_ids.get(p['id'], 0), projects.values()))
finish1 = time.perf_counter()
print("Результат: {}, время:{:.2}ms".format(result1, (finish1 - start1) * 1000))

start2 = time.perf_counter()
result2 = [p for p in projects.values() if projects_ids.get(p['id'], 0)]
finish2 = time.perf_counter()
print("Результат: {}, время:{:.2}ms".format(result2, (finish2 - start2) * 1000))