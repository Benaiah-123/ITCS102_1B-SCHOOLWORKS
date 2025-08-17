deposit= eval(input("enter the amount to deposit -->",))
print("here is the breakdown of the deposit amount: ")

thousand = deposit// 1000
deposit = deposit % 1000
fivehundred = deposit // 500
deposit = deposit % 500
twohundred = deposit // 200
deposit = deposit % 200
onehundred = deposit // 100
deposit = deposit % 100
fifty = deposit // 50
deposit = deposit % 50
twenty = deposit // 20
deposit = deposit % 20
ten = deposit // 10
deposit = deposit % 1-0
five = deposit // 5
deposit = deposit % 5
one = deposit // 1
deposit = deposit % 1

print(thousand,"-1000")
print(fivehundred,"-500")
print(twohundred,"-200")
print(onehundred,"-100")
print(fifty,"-50")
print(twenty,"-20")
print(ten,"-10")
print(five,"-5")
print(one, "-1")
 