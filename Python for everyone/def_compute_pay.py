
while True:
    try :    
        hours = float ( input ('please enter hours:'))       
        rate = float ( input ('please enter rate:'))
    except ValueError :
        print ('please enter a number')
        continue
    if hours < 0:
        print ('please enter hours as a positive number')
        if rate < 0:
            print ('please enter rate as a positive number')
        continue
    else:
        break
def computepay(hours, rate):
     if hours <=40:
         pay = hours * rate         
     else:  
         pay = 40 * rate + (hours - 40)* rate * 1.5
     return pay 
p = computepay(hours, rate)
print ('Pay' ,p)