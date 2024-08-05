import calendar

first_multiple_input = input().rstrip().split()

mm = int(first_multiple_input[0])
dd = int(first_multiple_input[1])
yyyy = int(first_multiple_input[2])
yy = yyyy%100

adjval1=1 if (calendar.isleap(yyyy) and (mm==1 or mm==2)) else 0
if (yyyy>=1800 and yyyy<1900):
    adjval2=2
if (yyyy>=1900 and yyyy<2000):
    adjval2=0
if (yyyy>=2000 and yyyy<2100):
    adjval2=-1
if (yyyy>=2100 and yyyy<2600):
    adjval2=4
if (yyyy>=2600 and yyyy<2700):
    adjval2=2
if (yyyy>=2700 and yyyy<2800):
    adjval2=0
if (yyyy>=2800 and yyyy<2900):
    adjval2=-1
if (yyyy>=2900 and yyyy<3400):
    adjval2=4

monthfactor=[1,4,4,0,2,5,0,3,6,1,4,6]
weekdays = ['SATURDAY','SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY']

aux = (yy+(yy//4)+dd+monthfactor[mm-1]-adjval1+adjval2)%7
print((str(dd)+'.'+str(mm)+'.'+str(yyyy)),weekdays[aux])

