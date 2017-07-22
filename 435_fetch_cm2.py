# This script downloads all the the (zipped) FEC detailed Committee Master data
# for House and Senate races, as found at the FEC:
# http://classic.fec.gov/finance/disclosure/ftpdet.shtml
#
# The result is a CSV file of the compiled records, from 1996 - 2016

from contextlib import closing
# the Requests library doesn't do FTP, thus, urlopen
from urllib.request import urlopen, Request
from zipfile import ZipFile
from io import BytesIO
from os.path import basename, join, splitext
import csv

YEARS = list(range(1996, 2016, 2)) # 2018 is excluded  - changed for detailed committee master file
HEADERS_URL = 'http://classic.fec.gov/finance/disclosure/metadata/cm_header_file.csv'  #changed from http://www.fec.gov/finance/disclosure/metadata/webl_header_file.csv'
# Note that this script only returns files from the Committee Master Files.
# You can modify the output of this helper function to get the other types of zip files

# Set up the output file
oname = "./cm-%s-%s.csv" % (YEARS[0], YEARS[-1])
output_csv = csv.writer(open(oname, 'w'))
# applying the headers defined by FEC
# the FEC site returns a 406 unless minimal headers are provided
hreq = Request(HEADERS_URL,  headers = {'Accept':'text/html'})
headers = urlopen(hreq).read().decode().strip().split(',')
# we'll add a "cycle" column to the top
headers.insert(0, 'cycle')
# write to the output file
output_csv.writerow(headers)

def url_for_year(year):
    """e.g. year=2014, result: 'ftp://ftp.fec.gov/FEC/2014/cm14.zip'"""
    y = str(year)
    return 'ftp://ftp.fec.gov/FEC/%s/cm%s.zip' % (y, y[2:])

## Download and write the data
# Iterate through YEARS to fetch all the FTP files
for yr in YEARS:
    zip_url = url_for_year(yr)
    with closing(urlopen(zip_url)) as r:
        print("Fetched:", zip_url)
        z = ZipFile(BytesIO(r.read()))
        rows = z.read(z.filelist[0]).decode().splitlines()
        for row in csv.reader(rows, delimiter = '|'):
            # insert cycle number
            row.insert(0, "%s" % (yr))  #"%s-%s" % (yr - 1, yr))
            # write to output file
            output_csv.writerow(row)
