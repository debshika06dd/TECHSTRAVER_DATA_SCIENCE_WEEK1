#Lists

food_order = ["Paneer Masala", "Butter Naan", "Jeera Rice", "Roasted Papad", "Dal Tadka"] #creating a list
print('\n')
print("Created List: ",food_order)


food_order.remove("Roasted Papad") #deleting element from the list
print("Deleting Roasted papad from the list: ", food_order)

food_order.reverse() #reversing the list 
print("Reversed List: ", food_order)

food_order.append("Masala Papad")
print("Adding Masala Papad to the list: ", food_order, '\n')

#Dictionaries

voter1 ={"name" : "Sunil", "gender" : "male", "age" : 22} #creating a dictionary
print("Created Dictionary: ", voter1)

del voter1["gender"] #deleting one of the key-pair
print("Key-pair gender deletion: " , voter1)

#Reverse not applicable for dictionaries

voter1["state"] = "Delhi" #appending a key-pair
print("Appended dictionary: ", voter1,'\n')

#Sets

visited_states = {'Punjab', 'Maharashtra', 'Delhi'} #creating set
print("Created Set: ", visited_states)

visited_states.remove('Maharashtra')
print("Deleting Maharashtra: ", visited_states) #deleting an element

#Reverse is not applicable for sets

visited_states.add('Gujarat')
print("Appended Set: ", visited_states, '\n') #appeding an element 

#Tuples
lucky_dates = (3, 10, 22) #creating tuple
print("Creating tuple: ", lucky_dates)

#Deletion is not possible in tuple

reversed_lucky_dates = lucky_dates[::-1]
print("Reversed tupple: ", reversed_lucky_dates , '\n')

#Appending is not possible in tuple







