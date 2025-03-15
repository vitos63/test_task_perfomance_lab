import json


def create_report(path_to_values:str, path_to_tests:str, path_to_report:str) -> None:
    with open(path_to_values) as file:
        values_data = json.load(file)

    values_dict = {item["id"]: item["value"] for item in values_data["values"]}

    with open(path_to_tests) as file:
        tests_data = json.load(file)

    tests_list = tests_data["tests"]

    update_values(values_dict, tests_list)

    report_data = {"tests": tests_list}

    with open(path_to_report, "w", encoding="utf-8") as file:
        json.dump(report_data, file)


def update_values(values_dict:dict, tests_list:list) -> None:
    for test in tests_list:
        id = test["id"]
        if id in values_dict:
            test["value"] = values_dict[id]

        if "values" in test:
            update_values(values_dict, test["values"])


path_to_values = input()
path_to_tests = input()
path_to_report = input()
create_report(path_to_values, path_to_tests, path_to_report)
