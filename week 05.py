from datetime import datetime,timedelta
daily_total_payment=0

try:
    while True:
      day=str(input("please enter day: ")).lower()
      if day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        break
      else:
         print("invalid input. please enter day.")    
    while True:
      try:
        hour,minute=map(int,input("enter hour of arrival(format: HH MM): ").split())
        if 8<=hour<=24 and  0<=minute<=60:
          break
        else:
         print("no parking is allowed between mindinght and 8:00.")
      except ValueError:
          print("invalid input.please enter valid time.")
    status_frequent_parking_num=input("Do you have frequent parking number please enter yes otherwise no. ")
    while status_frequent_parking_num not in['yes','no']:
       print("Invalid input. please enter either Yes or NO")
       status_frequent_parking_num = input("Do you have a frequent parking number? Please enter 'yes' or 'no': ")
    status_frequent_parking_num.lower()
    if status_frequent_parking_num=='yes':
        while True:
          frequent_parking_num_str = input("Enter frequent parking number: ")
          if len(frequent_parking_num_str) != 4:
               print("Invalid input. Please enter a 4-digit number.")
          elif not frequent_parking_num_str.isdigit():
               print("Invalid input. Please enter a numeric value.")
          else:
                weights=[4,3,2,1]
                product = sum(int(digit) * weight for digit, weight in zip(frequent_parking_num_str, weights))
                remainder=product%11
                if remainder>10:
                    print("Invalid frequent parking number. Check digit verification failed.")
                    frequent_parking_num_str=None
                else:
                   frequent_parking_num_str=True
                   break
    else:
       frequent_parking_num_str=None
    
    if 8<=hour<=15 and 0<minute<=59:
      while True:
       stay_in_hours_str=input("enter stay in hours: ")
       if not stay_in_hours_str.isdigit():
               print("Invalid input. please enter numeric value.")
       else:
           stay_in_hours=int(stay_in_hours_str)
           if stay_in_hours <= 0 or stay_in_hours > 24:
              print("Invalid input. hours can not be greater then 24 or less then 0.")
           else:
              break

      if day == 'sunday':
            max_stay_in_hours=8
            hours_total=hour+stay_in_hours
            hours_before_16=16-hour
            if hours_before_16 > max_stay_in_hours:
               print("maximum stay in hours are 8.")
            elif frequent_parking_num_str ==True:        
               if hours_total>=16:
                  price_per_hour=2
                  price_after_16_hours=2
                  total=hours_before_16*price_per_hour
                  discount_amount=0.10*total
                  discount_price=total-discount_amount
                  discount_amount_after_16=price_after_16_hours*0.50
                  discount_price_after_16=price_after_16_hours-discount_amount_after_16
                  discount_price+=discount_price_after_16
                  print("your total is",discount_price)
                  daily_total_payment += discount_price
               else:
                  price_per_hour=2
                  total=stay_in_hours*price_per_hour
                  discount_amount=0.10*total
                  discount_price=total-discount_amount
                  print("your total is",discount_price)
                  daily_total_payment += discount_price
            elif hours_total>=16:
                  price_per_hour=2
                  price_after_16_hour=2
                  total=hours_before_16*price_per_hour
                  total+=price_after_16_hour
                  print("your total is",total)
                  daily_total_payment+=total
            else:
               price_per_hour=2
               total=stay_in_hours * price_per_hour
               print("your total is",total)
               daily_total_payment += total
      elif day in ['monday','tuesday','wednesday','thursday','friday']:
            max_stay_in_hours=2
            hours_total=hour+stay_in_hours
            hours_before_16=16-hour
            if hours_before_16 > max_stay_in_hours:
                print("max stay in hours are 2.")
            elif frequent_parking_num_str ==True:
               if hours_total>=16:
                  price_per_hour=10
                  price_after_16_hours=2
                  total=hours_before_16*price_per_hour
                  discount_amount=0.10*total
                  discount_price=total-discount_amount
                  discount_amount_after_16=price_after_16_hours*0.50
                  discount_price_after_16=price_after_16_hours-discount_amount_after_16
                  discount_price+=discount_price_after_16
                  print("your total is",discount_price)
                  daily_total_payment += discount_price
               else:
                   price_per_hour=10
                   total=stay_in_hours*price_per_hour
                   discount_amount=0.10*total
                   discount_price=total-discount_amount
                   print("your total is",discount_price)
                   daily_total_payment += discount_price
            elif hours_total>=16:
                  price_per_hour=10
                  price_after_16_hour=2
                  total=hours_before_16*price_per_hour
                  total+=price_after_16_hour
                  print("your total is",total)
                  daily_total_payment+=total
            else:
               price_per_hour=10
               total=stay_in_hours*price_per_hour
               print("your total is",total)
               daily_total_payment += total
      if day =='saturday':
            max_stay_in_hours=4
            if hours_before_16 > max_stay_in_hours:
               print("max stay in hours are 4.")
            elif frequent_parking_num_str ==True:
               if hours_total>=16:
                  price_per_hour=3
                  price_after_16_hours=2
                  total=hours_before_16*price_per_hour
                  discount_amount=0.10*total
                  discount_price=total-discount_amount
                  discount_amount_after_16=price_after_16_hours*0.50
                  discount_price_after_16=price_after_16_hours-discount_amount_after_16
                  discount_price+=discount_price_after_16
                  print("your total is",discount_price)
                  daily_total_payment += discount_price
               else:
                  price_per_hour=3
                  total=stay_in_hours*price_per_hour
                  discount_amount=0.10*total
                  discount_price=total-discount_amount
                  print("your total is",discount_price)
                  daily_total_payment += discount_price
            elif hours_total>=16:
                  price_per_hour=3
                  price_after_16_hour=2
                  total=hours_before_16*price_per_hour
                  total+=price_after_16_hour
                  print("your total is",total)
                  daily_total_payment+=total
            else:
                price_per_hour=3
                total=stay_in_hours*price_per_hour
                print("your total is",total)
                daily_total_payment += total
    if 16<=hour<=24:
        stay_in_hours=int(input("enter stay in hours."))
        if stay_in_hours<=0 and stay_in_hours>24:
           print("invalid input. please enter valid stay in hours.")
        elif frequent_parking_num_str ==True:
           if day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            price=2
            total=price
            discount_amount=0.50*total
            discount_price=total-discount_amount
            print("your total is",discount_price)
            daily_total_payment += discount_price

        else:
          if day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            price=2
            total=price
            print("your total is",total)
            daily_total_payment+=total
    print("Daily total payment:",daily_total_payment)
except:
   print("Inavlid input. please try again.")



