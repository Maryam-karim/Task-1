import numpy as arr
# task 1
names_array=arr.array([],dtype='str')
for i in range(30):

        while True:
               name=str(input(f"Enter name of student no:{i+1} "))
               if name not in names_array:
                   names_array=arr.append(names_array,name)
                   break
               else:
                   print("This name is already written, please enter another name.")
weight_array=arr.array([],dtype='int')
for i in range(len(names_array)):
      try:
        while True:
           try: 
              weight=int(input(f"enter weight of {names_array[i]} in KG "))
              if weight!=0:
                 weight_array=arr.append(weight_array,weight)
                 break
              else:
                 print("This weight is not valid, please enter another weight.")
           except ValueError:
               print("this value is not valid, please enter another value.")
      except:
           print("invalid input,please try again.")
print("NAME OF STUDENT\t\t\t WEIGHT")
for element1,element2 in zip(names_array,weight_array):
    print(element1,"\t\t\t\t",element2)
# task 2
weight_array_lastDay=arr.array([],dtype='int')
for i in range(len(names_array)):
      try:
        while True:
           try: 
              weight=int(input(f"enter weight of {names_array[i]} in KG on the last day "))
              if weight!=0:
                 weight_array_lastDay=arr.append(weight_array_lastDay,weight)
                 break
              else:
                 print("This weight is not valid, please enter another weight.")
           except ValueError:
               print("this value is not valid, please enter another value.")
      except:
           print("invalid input,please try again.")
# task 3
difference_array=arr.array([],dtype='int')
difference=weight_array_lastDay - weight_array
difference_array=arr.append(difference_array,difference)

for i,rise in enumerate(difference_array):
      if rise>2.5:
        print(f"There is increase in weight of {names_array[i]} of {rise} KG")
for i,fall in enumerate(difference_array):
    if fall<-2.5:
         print(f"There is decrease in weight of {names_array[i]} of {fall} KG")
   

      
          


          
     


                


           
    

