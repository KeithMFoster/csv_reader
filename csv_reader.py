import csv
import datetime

f = open('myfile.csv', 'w')

with open('member_dump.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    my_row = 0
    duplicate = ''
    dup = ''

    for row in readCSV:
        my_row = my_row + 1

        id = row[0]
        cst_key = row[1]

        if dup == cst_key:
            duplicate = 'X'
        else:
            duplicate = ''

        dup = cst_key
        first_name = row[2]
        last_name = row[3]
        email = row[4]
        recno = row[5]
        mbt_code = row[6]
        web_login = row[7]
        designation = row[8]
        full_name = row[9]
        membership_expire_date = row[10]
        myline = str(my_row) + ',' + duplicate + ',' + str(id) + ',' + cst_key + ',"' + first_name + '","' + last_name + '","' + email + '",' + recno + ',"' + mbt_code + '","' + web_login + '","' + designation+'","' + full_name + '","' + membership_expire_date + '"\n'

        f.write (myline)
# id, cst_key, first_name, last_name, email, recno, mbt_code, web_login, designation, full_name, membership_expire_date


f.close()  # you can omit in most cases as the destructor will call it
