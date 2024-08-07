import csv

def parse_spec(file_path):
    spec = []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.split()
            field_name = parts[0]
            field_length = int(parts[1])
            spec.append((field_name, field_length))
    return spec

def parse_fixed_width(spec, input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow([field[0] for field in spec])  # Write header

        for line in infile:
            pos = 0
            row = []
            for field_name, field_length in spec:
                field_value = line[pos:pos+field_length].strip()
                row.append(field_value)
                pos += field_length
            writer.writerow(row)

if __name__ == '__main__':
    spec = parse_spec('spec.txt')
    parse_fixed_width(spec, 'data.fwf', 'output.csv')
