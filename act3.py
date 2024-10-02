print("enter marks obtained in 5 subjects: ")
mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())

total= mark1+mark2+mark3+mark4+mark5
avg=total/5

if avg>=91 and avg<=100:
    print("your grade is a1")
elif avg>=81 and avg<=91:
    print("your grade is a2")
elif avg>=71 and avg<=81:
    print("your grade is b1")
elif avg>=61 and avg<=71:
    print("your grade is b2")
elif avg>=51 and avg<=61:
    print("your grade is c1")
elif avg>=41 and avg<=51:
    print("your grade is c2")
elif avg>=31 and avg<=41:
    print("your grade is d")
elif avg>=21 and avg<=31:
    print("your grade is e1")
elif avg>=0 and avg<=21:
    print("your grade is e2")
else:
    print("invalid input")