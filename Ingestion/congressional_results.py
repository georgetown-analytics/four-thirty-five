import requests
import pandas as pd
import openpyxl


year = list(range(2002, 2016, 2))
sheets = ['%s US House & Senate Results'] % (year) # add corresponding sheet names
dfs = []
for (year,sheet) in zip(years,sheets):
    xls ='https://transition.fec.gov/pubrec/fe'+ year + '/federalelections' + year + '.xls'
    resp = requests.get(xls)
    filename = 'file' + year + '.xls'
    output = open(filename,'wb')
    output.write(resp.content)
    output.close()

    df = pd.read_excel(filename,sheetname=sheet)
    df['YEAR'] = len(df) * [year]
    newfilename = 'new' + year + '.xlsx'
    df.to_excel(newfilename,index=False)

    # need to rename some columns for each year: use dictionary format
    # so when you concat the dataframes they match up correctly
    # currently columns from dif--ferent years that have the same context are not
    # concatenating as the same column
    dfs.append(df)


master = pd.concat(dfs)
master.to_excel('master_file.xlsx',index=False)
