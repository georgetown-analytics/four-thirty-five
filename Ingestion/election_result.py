from __future__ import print_function
from contextlib import closing
from urllib.request import urlopen, Request
from os.path import join, dirname, abspath
import csv
import pandas as pd
import numpy as np
import xlrd

YEARS = list(range(2002, 2016, 2)) # 2016 is excluded  - changed for detailed committee master file
oname = "./election-%s-%s.csv" % (YEARS[0], YEARS[-1])


def url_for_year(year):
    """e.g. year=2014, result: 'https://transition.fec.gov/pubrec/fe2012/federalelections2012.xls'"""
    y = str(year)
    return 'https://transition.fec.gov/pubrec/fe%s/federalelections%s.xls' % (y, y[2:])

## Download and write the data
# Iterate through YEARS to fetch all the FTP files
for yr in YEARS:
    results_url = url_for_year(yr)
    print("Fetched:", results_url)




    fname = join(dirname(dirname(abspath(__file__))), 'test_data', results_url)
    xl_workbook = xlrd.open_workbook(fname)
    sheet_names = xl_workbook.sheet_names()
    sheet_results = book.sheet_by_names(%s "US HOUSE & SENATE RESULT") % (yr)

def election_result(year):
    results_2004 =

output_csv = csv.writer(open(oname, 'w'))
DataFrame.to_csv(oname)
df = pd.read_csv(oname)
df.to_excel(writer, sheet_name='election')
writer.save()
