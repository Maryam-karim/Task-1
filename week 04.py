def auction_set_up():
    items=[]
    keep_going='y'
    try:
       while keep_going.lower()=='y': 
             item_number=int(input("enter item number: "))
             if any(item['item_number'] == item_number for item in items):
                 print("item number already exists.please enter another item number.")
                 continue
             description=input(f"enter description of item number:{item_number} ")
             reserve_price=int(input(f"enter reserve peice of item number:{item_number} "))
             number_of_bids=0
             items.append({'item_number':item_number,"description":description,"reserve_price":reserve_price})
             keep_going=input("do you want to enter information of another item. press y for yes and no for termination.")
             
       if len(items) >= 1:
            return items
       else:
            print("Items are not enough for the auction. Please add more items.")
    except ValueError:
      print("Invalid input.please try again.")
      return auction_set_up()
def displaying_information(items):
    print("\n\n\t\t\tList of all the items in the auction:")
    for item in items:
        print(f"\t\t\tItem number: {item['item_number']}")
        print(f"\t\t\tDescription: {item['description']}")
        print(f"\t\t\tReserve price: {item['reserve_price']}$")
        print("-" * 60) 
def buyer_input(items):
    buyer_info=[]
    keep_going='y'
    while keep_going.lower()=='y':
       item_found=False
       try:
           buyer_num = int(input("Enter buyer num: "))
           item_number = int(input("Enter item number for which you want to bid: "))
           for item in items:
            if item['item_number'] == item_number:
              bid = int(input("Enter bid amount: "))
              if bid > item.get('highest_bid', 0):
                item['highest_bid'] = bid
                buyer_info.append({'item_number':item_number,'highest_bid':bid})
                print("Bid successfully placed!")
              else:
                print(f"Bid amount should be higher than the current highest bid {item['highest_bid']}$.")
              item_found=True
              break
            if not item_found:
             print("There is no item with this item number.")
             break
       except ValueError:
            print("invalid input.please try again.")

       keep_going=input("do you want to bid for another item. if yes press 'y' else 'n' for no.")
    return buyer_info
def result_auction(items, buyer_info):
    total_fee=0
    for item in items:
        item_has_bid=False
        for bid in buyer_info:
            if item['item_number'] == bid['item_number']:
                item_has_bid=True
                if item['reserve_price'] == bid['highest_bid']:
                  print(f"Item number: {item['item_number']} is sold.")
                  fee=bid['highest_bid']*0.10
                  total_fee+=fee
                elif bid['highest_bid'] < item['reserve_price']:
                   print(f"item number{item['item_number']} with bit amount of{bid['highest_bid']} have not reached their reserved price.")
            if not item_has_bid:
                print(f"Item number {item['item_number']} has zero bids.")
                
    print("total fee for all sold items is",total_fee)

def main():
    auction_initial_info= auction_set_up() 
    displaying_information(auction_initial_info)  
    buyer_info=buyer_input(auction_initial_info)
    result_auction(auction_initial_info,buyer_info)
main()
