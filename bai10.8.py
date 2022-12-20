import calendar
y=int(input("Please enter year:"))
m=int(input("Please enter month:"))
d=int(input("Please enter day:"))
note1=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#xuaast ngày tháng
print("Day/Month/Year:",d,"/",m,'/',y)
#thứ
print("This day is",note1[calendar.weekday(y,m,d)])
#tính năm nhuận
def year(y):
    year=dict()
    year[0] =y%4
    year[1] =y%10
    return year
year=year(y)
if year[0]==0:
    print(y,'is leap year')
elif year[1]!=0: 
    print(y,"isn't leap year")
#tính số ngày có trong tháng
print(calendar.month(y,m))
note2=calendar.monthrange(y,m)
note3=list(note2)
print("Number of days in month is",note3[1])
