import sys
import csv

def main():
    x, y = argv_check()
    conv_names(x, y)

def argv_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    x = sys.argv[1]
    y = sys.argv[2]

    if not x.endswith('.csv') or not y.endswith('.csv'):
        sys.exit("Not a CSV File")

    return x, y

def conv_names(x, y):
    with open(x, "r") as file, open(y, "w", newline='') as after:
        reader = csv.DictReader(file)
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(after, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow({
                'first': first,
                'last': last,
                'house': row['house']
            })

if __name__ == "__main__":
    main()
