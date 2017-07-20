import csv
def get_csvData(fileName):
    #create an empty list to store rows
    rows=[]
    #open the csv file
    datafile=open(fileName,'r')
    #create reader
    reader=csv.reader(datafile)
    #skip the first row as it is not the data that we want to supply
    next(reader)
    # Add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows


# print(get_csvData(r'C:\Users\MEGHA\PycharmProjects\DOMFRMWRKEX\Files\course_selection_data.csv'))