mylist=int(input("enter the no of list"))
a=[]
for i in range(mylist):
    b=int(input("enter the no of list"))
    a.append(b)
if len(a)<3:
  print("enter the three element in list")
else:
  sorted_list=sorted(a,reverse=True)
  print(sorted_list)
  three_list=sorted_list[:3]
  print(three_list)
