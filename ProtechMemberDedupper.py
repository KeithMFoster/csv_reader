import csv
import datetime
import operator
from calendar import monthrange


today = datetime.datetime.now()
d3 = today.strftime("%m-%d-%Y_%H:%M:%S")
print("d3 =", d3)


def last_day_of_month(date_value):
    return date_value.replace(day=monthrange(date_value.year, date_value.month)[1])

# EntryCounts,inv_cst_key,ContactNumber,AccountNumber,MembershipType,CycleStartDate,PaidThroughDate,JoinedDate,RejoinedDate,BenefitStatus,TerminationDate,LegacyMembershipType,(temp) name

with open('Protech Member Query V5a.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV, None)
    # sortedcsv = sorted(readCSV, key=operator.itemgetter(0, 3))
    my_row = 0
    myline = ''
    event = ''

    oentrycounts = 0
    oinv_cst_key = ''
    ocontactnumber = ''
    oaccountnumber = ''
    omembershiptype = ''
    ojoineddate = ''
    opaidthroughdate = ''
    ocyclestartdate = ''
    orejoineddate = ''
    obenefitstatus = ''
    oterminationdate = ''
    olegacymembershiptype = ''
    oname = ''
    current_contactnumber = ''
    current_accountnumber = ''
    line_count = 0
    mycount = 0
    myjoineddate = ''
    savedjoineddate = ''
    lame = ''
    bob = ''
    sam = []
    f = open('member_output_' + d3 + '.csv', 'w')
    t = open('terminated.csv', 'w')

    myline = 'ContactNumber, AccountNumber, MembershipType, CycleStartDate, PaidThroughDate, JoinedDate, ' \
             'RejoinedDate, BenefitStatus, TerminationDate, LegacyMembershipType, (temp) name, bob\n'
    f.write(myline)

    for row in readCSV:
        bob = row
        entrycounts = int(row[0])
        cycleenddate = row[1]
        contactnumber = row[2]
        accountnumber = row[3]
        membershiptype = row[4]
        cyclestartdate = row[5]
        paidthroughdate = row[6]
        joineddate = row[7]
        rejoineddate = row[8]
        benefitstatus = row[9]
        terminationdate = row[10]
        legacymembershiptype = row[11]
        name = row[12]

        if bob != sam:
            line_count = 1
            ocycleenddate = cycleenddate
            oentrycounts = entrycounts
            ocontactnumber = contactnumber
            oaccountnumber = accountnumber
            omembershiptype = membershiptype
            ojoineddate = joineddate
            opaidthroughdate = paidthroughdate
            orejoineddate = rejoineddate
            obenefitstatus = benefitstatus
            oterminationdate = terminationdate
            olegacymembershiptype = legacymembershiptype
            oname = name
            sam = bob

            if current_contactnumber != contactnumber:
                # ok, new person now.
                mycount = 1
                current_contactnumber = contactnumber

                lame = 'X'
                bob = '1'
                print('===> New Contact Number ' + contactnumber)
                if benefitstatus != 'TERMINATED':
                    benefitstatus = 'NEW'

                if entrycounts == 1 and terminationdate != 'NULL':
                    benefitstatus = 'TERMINATED'
                    bob = 'One Liner'
                    myjoineddate = joineddate
                    savedjoineddate = joineddate
                else:
                    bob = 'First Line'
                    myjoineddate = joineddate
                    savedjoineddate = joineddate

                    if benefitstatus == 'NEW' and terminationdate != 'NULL':
                        terminationdate = ''


                if benefitstatus == 'NEW' and terminationdate == 'NULL' :
                    terminationdate = ''

                print(contactnumber + ' <> ' + paidthroughdate)

            elif current_accountnumber != accountnumber and contactnumber == '':
                # ok, new person now.
                mycount = 1
                lame = ''
                bob = '2'
                current_accountnumber = accountnumber
                print('===> New Account Number ' + accountnumber)
                if benefitstatus != 'TERMINATED':
                    benefitstatus = 'NEW'
                print(accountnumber + ' <> ' + paidthroughdate)
            else:
                mycount = mycount + 1
                lame = ''
                bob = 'else'

                if benefitstatus == 'RENEW' and rejoineddate == 'NULL':
                    myjoineddate = savedjoineddate
                elif benefitstatus == 'RENEW' and rejoineddate != 'NULL':
                    newrejoineddate = datetime.datetime.strptime(rejoineddate, '%Y-%m-%d')
                    newstartdate = datetime.datetime.strptime(cyclestartdate, '%Y-%m-%d')
                    newenddate = datetime.datetime.strptime(paidthroughdate, '%Y-%m-%d')

                    if newrejoineddate <= newenddate and newrejoineddate >= newstartdate:
                        myjoineddate = rejoineddate
                        savedjoineddate = rejoineddate

                elif benefitstatus == 'RENEW' and terminationdate != 'NULL':
                    newtermination = datetime.datetime.strptime(terminationdate, '%Y-%m-%d')
                    newstartdate = datetime.datetime.strptime(cyclestartdate, '%Y-%m-%d')
                    newenddate = datetime.datetime.strptime(paidthroughdate, '%Y-%m-%d')
                    if newtermination <= newenddate and newtermination >= newstartdate:
                        benefitstatus = 'TERMINATED'

                if benefitstatus != 'TERMINATED':
                    terminationdate = ''


            myline = contactnumber + ',' + accountnumber + ',"' + membershiptype + '",' + cyclestartdate + ',' +\
                     paidthroughdate + ',' + joineddate + ',' + myjoineddate + ',' + benefitstatus + ',' \
                     + terminationdate + ',"' + legacymembershiptype + '","' + name + '","' + bob + '"\n'

            f.write(myline)


        else:
            line_count = line_count + 1

    f.close
    t.close