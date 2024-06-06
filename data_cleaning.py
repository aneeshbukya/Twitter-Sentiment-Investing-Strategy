import csv

# Input and output file paths
input_file_path = 'sentiment_data.csv'
output_file_path = 'sentiment_data_new.csv'

# Word to filter out
filter_word = 'ATVI'

# Open the input file for reading and output file for writing
with open(input_file_path, mode='r', newline='') as infile, open(output_file_path, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Iterate over each row in the input file
    for row in reader:
        # Check if the filter word is in any of the row's cells
        if filter_word not in row:
            # Write the row to the output file if it doesn't contain the filter word
            writer.writerow(row)

print(f"Rows containing '{filter_word}' have been removed and the cleaned data is saved to '{output_file_path}'.")
