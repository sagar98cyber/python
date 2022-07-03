fileName = "data.csv"

with open(fileName, "rb") as in_file, open("out.csv", "wb") as out_file:
    out_file.write(in_file.read())