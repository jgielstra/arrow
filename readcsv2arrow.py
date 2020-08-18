from pyarrow import csv, RecordBatchFileWriter
file = 'monroe-county-crash-data2003-to-2015.csv.gz'
table = csv.read_csv(file)
print(table)
with open('monrow-crash.arrow', 'bw') as f:
    writer = RecordBatchFileWriter(f, table.schema)
    writer.write(table)
    writer.close()