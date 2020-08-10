import csv
import sys
import argparse

'''
two positional arguments for the input file and the output file
two named arguments
--in-delimiter="|"
--in-quote="'"
'''

def fix_csv(infile: str, outfile: str, delimiter: str, quotechar: str):
    with open(infile, 'r') as inf:

        # try to detect
        try:
            custom_dialect = csv.Sniffer().sniff(inf.read(1024))
            # print("debug: successfully sniffed dialect")
            # print(f"quotechar: {custom_dialect.quotechar}")
            # print(f"delimiter: {custom_dialect.delimiter}")
        except:
            # print("debug: could not sniff dialect")
            custom_dialect = 'excel'
        finally:
            inf.seek(0)

        # allow user override
        if delimiter or quotechar:    
            if delimiter:
                # print(f"setting custom delimiter of {delimiter}")
                custom_dialect.delimiter = delimiter
            if quotechar:
                # print(f"setting custom quotechar of {quotechar}")
                custom_dialect.quotechar = quotechar
        
        reader = csv.reader(inf, dialect=custom_dialect)
        with open(outfile, 'w', newline='') as outf:

            writer = csv.writer(outf, delimiter=',') 
            for row in reader:
                line = []
                for item in row:
                    line.append(item)
                writer.writerow(line)
            


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a delimiter-separated input file into a comma separated one.')
    parser.add_argument('infile', help='path to output file')
    parser.add_argument('outfile', help='path to input file')

    parser.add_argument('--in-delimiter', dest='delimiter', help='delimiter used in input file')
    parser.add_argument('--in-quote', dest='quotechar', help='style of quote mark used in input file')
    args = parser.parse_args()
    
    infile = args.infile
    outfile = args.outfile

    # print(f"infile detected as {infile}")
    # print(f"outfile detected as {outfile}")

    fix_csv(infile, outfile, args.delimiter, args.quotechar)