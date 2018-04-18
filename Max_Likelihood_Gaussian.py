import csv
import numpy

def readfile(filename):
    input_file = csv.DictReader(open(filename))
    rows = list(input_file)
    a = 0
    values = []
    a1 = 0
    values1 = []
    a2 = 0
    values2 = []

    for line in rows:
            weightstr2 = line["Weight"]
            a2 += float(weightstr2)
            values2.append(float(weightstr2))

    print("1) The mean, is {}, variance is {}".format(numpy.mean(values2), numpy.var(values2, axis=0)))


    for line in rows:
        if line["GP_greater_than_0"] == 'yes':
            weightstr = line["Weight"]
            a += float(weightstr)
            values.append(float(weightstr))

    print("2) The mean when GP_greater_than_0 is yes, is {}, variance is {}".format(numpy.mean(values), numpy.var(values, axis=0)))


    for line in rows:
        if line["GP_greater_than_0"] == 'no':
            weightstr1 = line["Weight"]
            a1 += float(weightstr1)
            values1.append(float(weightstr1))

    print("3) The mean when GP_greater_than_0 is no, is {}, variance is {}".format(numpy.mean(values1), numpy.var(values1, axis=0)))



if __name__ == "__main__":
        readfile('data1.csv')
