# WRITE YOUR FUNCTIONS HERE

#Q1


def get_pet_shop_name(name):
    return name["name"]

#Q2
def get_total_cash(sum):
    return sum["admin"]['total_cash']

#Q3 - doesn't need to return anything as test checks against dict value. Only need to alter dict value
def add_or_remove_cash(total, transaction):
    total["admin"]["total_cash"] += transaction

#Q4
def add_or_remove_cash(total, transaction):
    total["admin"]["total_cash"] += transaction

#Q5
def get_pets_sold(sales):
    return sales["admin"]["pets_sold"]

#Q6
def increase_pets_sold(sales,increase):
    sales["admin"]["pets_sold"] += increase

#Q7
def get_stock_count(count):
   return(len(count["pets"]))

#Q8
def get_pets_by_breed(shop,breed):
    count = []
    length = len(shop["pets"])
    for check in range(0,length,1):
        if shop["pets"][check]["breed"] == breed:
            count.append(shop["pets"][check]["breed"])
    return count
#Q9
def get_pets_by_breed(shop,breed):
    count = []
    length = len(shop["pets"])
    for check in range(0,length,1):
        if shop["pets"][check]["breed"] == breed:
            count.append(shop["pets"][check]["breed"])
            
    return count

#Q10 - 'NoneType object is not subscriptable' can't figure out. The syntax makes it look like I'm supposed to pass the test a list
#but no matter what I pass (value, list, key, dictionary) I keep getting the NoneType. What am I missing here?
def find_pet_by_name(shop,name):
    
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet

    
    

#Q11
# def find_pet_by_name(shop,name):
#     count = []
#     length = len(shop["pets"])
#     for check in range(0,length,1):
#         if shop["pets"][check]["name"] == name:
#             count.append(shop["pets"][check]["name"])
#             return count
#         else:
#             return None

#Q12
def remove_pet_by_name(shop,name):
    pet_to_delete = find_pet_by_name(shop, name)
    shop["pets"].remove(pet_to_delete)

    # length = len(shop["pets"])
    # for check in range(0,length,1):
    #     if shop["pets"][check]["name"] == name:
    #         shop["pets"][check]["name"] = None
    #     else:
    #         pass

#Q13
def add_pet_to_stock(shop,new_pet):
    shop["pets"].append(new_pet)

    
#Q14
def get_customer_cash(client):
    monies = client["cash"]
    return monies

#Q15
def remove_customer_cash(customer,cash):
    customer["cash"] -= cash

#Q16
def get_customer_pet_count(customer):
    if customer["pets"] == []:
        return 0
    else:
        return (len([customer["pets"]]))

#Q17
def add_pet_to_customer(customer,pet):
    customer["pets"].append(pet)
    #print(customer)
    

############################################################################
#Extensions
#Q1,2 & 3
def customer_can_afford_pet(customer,pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False

#Q4 - not sure how to print individual error messages in repsonse to a failed test if we can't edit the test sheet
#If (pun intended) we were allowed to alter the test sheet I would put an if statement around the tests and say if True print x or if False print y


def sell_pet_to_customer(shop,pet,customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(shop, pet["price"])
        increase_pets_sold(shop, 1)
        print("Congratulations, you now own a pet!")


