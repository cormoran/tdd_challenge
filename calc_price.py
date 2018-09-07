from tax import calc_price
import sys


def calc_price_stream(fin, fout):
    read = fin.read()
    if read.count("\n") == len(read):
        read = read[:-1]
        if len(read) == 0:
            fout.write("\n")

    for line in read.split("\n")[:-1]:
        if len(line) == 0:
            values = []
        else:
            values = list(map(int, line.split(',')))
        fout.write(str(calc_price(values)) + "\n")


if __name__ == "__main__":
    calc_price_stream(fin=sys.stdin, fout=sys.stdout)
