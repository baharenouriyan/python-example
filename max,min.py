
 #یک لیست عدد بده و بزرگ ترین و کوچک ترین عدد رو پیدا کن
number=[3,6,13,87,59,43,2]
max_num =number[0]
min_num =number[0]
for num in number :
  if num >max_num :
    max_num=num
  if num <min_num :
    min_num=num
    print("max",max_num)
    print("min",min_num)