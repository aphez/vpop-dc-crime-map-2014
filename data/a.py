import csv

files = ["dc_wards578_houses.csv", "dc_wards578_houses.csv.h2o"]
ldata = []

for file in files:
    with open(file, "r") as f_input:
        csv_input = csv.reader(f_input, delimiter="\t", skipinitialspace=True)
        set_rows = set()
        for row in csv_input:
            set_rows.add(tuple(row))
        ldata.append(set_rows)

with open("Intersection(Brachypodium_Japonica).csv", "w") as f_output:
    csv_output = csv.writer(f_output, delimiter="\t", skipinitialspace=True)
    csv_output.writerows(set.intersection(*ldata))