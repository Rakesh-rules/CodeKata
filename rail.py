import datetime
station = ('chennai','pondy','madurai','covai','bangalore')
#station is a tuple that has a list of stations.
shedule={1:('1:00','chennai','pondy'),2:('2:00','chennai','pondy')}
#shedule is a dictionary that holds train number, time, from and to stations
date={'2017-02-10':(1,3,4,5),'2018-02-11':(2,4,6)}
#date is a dictionary that holds the list of traind in that a particular date
a=1
for x in station:
    print (a,".",x)
    a+=1
a=1
#prints the list of station with a number. to eliminate the use of GUI
f=input("Enter from city number")
#Enter the city number from above list to enter starting city
t=input("Enter to city number")
#Enter the city number from above list to enter destination city
date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
for y in shedule:
    while(shedule[y][1]==station[int(f)-1] and shedule[y][2]==station[int(t)-1] and y in date[str(date1)][:]):
        print(shedule[y][0]+"\t"+shedule[y][1]+"\t"+shedule[y][2]+"\n")
        break
#This will print a list of stations from shedule which operates on that particular date
