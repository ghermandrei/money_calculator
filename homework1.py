money=int(input('enter $  '))
 

bills_20=money//20 
bills_5=(money-(bills_20*20))//5
bill_1=money-(bills_20*20+bills_5*5)

print(bills_20,"x 20",bills_5, "x 5$",bill_1,"x 1$")

 

