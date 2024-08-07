import csv
import hashlib

def anonymize(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def anonymize_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            row['first_name'] = anonymize(row['first_name'])
            row['last_name'] = anonymize(row['last_name'])
            row['address'] = anonymize(row['address'])
            writer.writerow(row)

if __name__ == '__main__':
    anonymize_csv('data.csv', 'anonymized.csv')
