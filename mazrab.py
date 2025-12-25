#اعداد یک تا سی رو مضرب هاشون رو چاپ کن

for i in range(1,30):
    if i %4==0 :
          print(i,"four")
    elif i %6==0 :
          print("six")
    elif i %4==0 and i%6==0 :
         print("foursix")
    else :
         print(i)