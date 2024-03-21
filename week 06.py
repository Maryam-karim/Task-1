from prettytable import PrettyTable
import uuid
ticket_table = PrettyTable()
ticket_table.field_names =[" Ticket type","Cost for one Day","Cost for two days","Days available for booking"]
ticket_table.add_row(["one adult","$20.00","$30.00","Monday to Saturday"])
ticket_table.add_row(["one child (an adult may bring up to two children)"," $12.00","$18.00","Monday to Saturday"])
ticket_table.add_row([" one senior"," $16.00","$24.00","Monday to Saturday"])
ticket_table.add_row(["family ticket (up to two adults or seniors, and three children)","$60.00","$90.00","Monday to Saturday"])
ticket_table.add_row([" groups of six people or more, price per person","$15.00","$22.50","Monday to Saturday"])
print(ticket_table)
attractions_table=PrettyTable()
attractions_table.field_names=["Extra attraction","cost per person"]
attractions_table.add_row(["lion feeding","$2.50"])
attractions_table.add_row(["penguin feeding","$2.00"])
attractions_table.add_row([" evening barbecue (two-day tickets only)","$5.00"])
print(attractions_table)
booked_ticket=[]

while True:
  try:
    ticket_booking_dayNum=int(input("Do you want to book Ticket for one day or two consecutive days? Enter 1 for one day and 2 for Two days. "))
    if ticket_booking_dayNum not in[1,2]:
         print("you can book a visit of only 1 or 2 days.")
         continue
  except:
    print("Invalid input. please enter valid input.")
    continue
  print("Please enter the number of adults, seniors, and children who are coming for the visit, so we can allocate the corresponding ticket type.")
  while True:
   
   booked_tickets = []
   try:
    num_adults=int(input("enter number of adults."))
    num_children=int(input("enter number of children."))
    num_seniors=int(input("enter number of seniors."))
   except:
     print("Invalid input. please enter valid input.")
     continue
   total_person=num_adults+num_children+num_seniors
   children_per_adult=num_children/2
   if  num_adults<children_per_adult:
            print("Sorry, children cannot visit without adults or one adult can take two childrens.")
            continue
   total_seniorAdult=num_adults+num_seniors
   if num_adults % 2 == 0 and num_children % 3 == 0:
      condition_total=num_adults//2 or num_seniors//2
      ticket_total = 60*condition_total if ticket_booking_dayNum == 1 else 90
      booked_tickets.append(ticket_total)
      if num_seniors >= 1:
        senior_total = num_seniors * (16 if ticket_booking_dayNum == 1 else 24)
        booked_tickets.append(senior_total)
      else:
          break
   else:
    if 1 <= num_adults <= 5:
        adult_total = num_adults * (20 if ticket_booking_dayNum == 1 else 30)
        booked_tickets.append(adult_total)
    
    if num_seniors >= 1:
        senior_total = num_seniors * (16 if ticket_booking_dayNum == 1 else 24)
        booked_tickets.append(senior_total)
    
    if num_adults >= 6:
        group_total = num_adults * (15 if ticket_booking_dayNum == 1 else 22.50)
        booked_tickets.append(group_total)
    elif num_adults % 2 == 0 and num_seniors % 2 == 0:
        group_total = num_adults * (15 if ticket_booking_dayNum == 1 else 22.50)
        booked_tickets.append(group_total)
    
    if num_children >= 1:
        children_total = num_children * (12 if ticket_booking_dayNum == 1 else 18)
        booked_tickets.append(children_total)

   print(booked_tickets)



   booked_attractions=[]
   while True:
      try:
         ticket_booking_attraction_name = input("Enter attraction for which you want to book ticket for (or enter 'done' to finish): ").lower()
         num_people_going_for_attraction=int(input("enter how many people are going for attractions."))
         if num_people_going_for_attraction>total_person:
                print(f"the number of tickets you bought are {num_people_going_for_attraction}: ")
                continue
         if ticket_booking_attraction_name == "done":
             break
         elif ticket_booking_attraction_name=="lion feeding":
            total_attraction=num_people_going_for_attraction*2.50
            booked_attractions.append(total_attraction)
         elif ticket_booking_attraction_name=="penguin feeding":
             total_attraction=num_people_going_for_attraction*2.00
             booked_attractions.append(total_attraction)
         elif ticket_booking_attraction_name == "barbecue" or ticket_booking_attraction_name == "bbq" or ticket_booking_attraction_name == "evening barbeque" or ticket_booking_attraction_name == "evening bbq":
            total_attraction=num_people_going_for_attraction*5.00
            booked_attractions.append(total_attraction)
         else:
               print("Attraction not found. Please enter a valid attraction.")
      except:
        print("Invalid input. please enter valid input")
        continue
      another=input("do you want to buy a ticket for another attraction. please enter yes and no.")
      if another=="yes":
          continue
      else:
          break
   total_attraction_cost = sum(booked_attractions)
   total_booking_ticket=sum(booked_tickets)
   print(booked_tickets)
   net_total=total_attraction_cost+total_booking_ticket
   booking_num = str(uuid.uuid4())
   print("Your booking number is:", booking_num)
   print(booked_ticket)
   print(f"you book a visit of {ticket_booking_dayNum} day and your total amount is {net_total}$.")
 

