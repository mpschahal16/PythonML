#if else ladder
year=(int)(input("Enter the year :"))
if(year%400==0):
    print(year, " is leap year")
elif(year%4==0 and year%100!=0):
    print(year ," is leap year")
else:
    print(year ,"is not a leap year")


'''
#O/P
Enter the year :1700
1700 is not a leap year
'''