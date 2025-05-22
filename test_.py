from tabulate import tabulate

data = [
    {"BATCH": "1st", "BATCH ID": "212-134-***"},
    {"BATCH": "2nd", "BATCH ID": "221-134-***"},
    {"BATCH": "3rd", "BATCH ID": "222-134-***"},
    {"BATCH": "4th", "BATCH ID": "231-134-***"},
    {"BATCH": "5th", "BATCH ID": "232-134-***"},
    {"BATCH": "6th", "BATCH ID": "241-134-***"},
    {"BATCH": "7th", "BATCH ID": "242-134-***"},
    {"BATCH": "8th", "BATCH ID": "251-134-***"},
    {"BATCH": "9th", "BATCH ID": "252-134-***"}
]

print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
