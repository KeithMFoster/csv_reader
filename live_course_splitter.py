import csv
import datetime

with open('live_data_export.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    my_row = 0
    myline = ''
    event = ''
    f = open('start.csv', 'w')

    for row in readCSV:
        recno = row[0]
        first_name = row[1]
        last_name = row[2]
        email = row[3]
        member_type = row[4]
        credits_taken = row[5]
        certificate = row[6]
        mydate = row[7]
        event_name = row[8]

        if event != event_name:
            f.close
            event = event_name
            f = open(event+'.csv', 'w')
            myline =  '"ID number","First Name","Last Name","Email Address","Member Type","Credits Taken","Certificate","Date Issued","Event Name"\n'
            f.write(myline)

            myline = recno + ',"' + first_name + '","' + last_name + '","' + email + '","' + member_type + '",' + credits_taken + ',"' + certificate + ',"' + mydate + '","' + event_name + '"\n'
            f.write(myline)
        else:
            myline = recno + ',"' + first_name + '","' + last_name + '","' + email + '","' + member_type + '",' + credits_taken + ',"' + certificate + ',"' + mydate + '","' + event_name + '"\n'
            f.write(myline)