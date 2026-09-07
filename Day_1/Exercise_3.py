import math

"""problem 1 
Write an example for different Python data types such as
Number(Integer, Float, Complex), 
String, Boolean, List,
Tuple, Set and Dictionary."""
Numb_int =1
Numb_Float =1.0
Numb_complex =1J
first_String = 'my first string'
first_Bolean = True
# Boleans are variables that hold only Ture or False
first_List= [0,1,2,'A','B','C', True]
#A list is an ordered collection of data of any type
first_Tuple = (1,2,3)
#siialer to a list but it can not be edited
first_set = {1,2,3}
# a collection of data in mathematics not orderd and can only contain one value once
first_Directory = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'country':'Finland',
    'age':250,
    'is_married':True,
    'skills':['JS', 'React', 'Node', 'Python']
}
# a collection of unorderd data that is marked by a key value
"""
Find an Euclidean distance between (2, 3) and (10, 8)
"""
cord_1 = (2.0,3.0)
cord_2 = (10.0,8.0)
distance = math.sqrt(((cord_1[0]-cord_2[0])**2)+((cord_1[1]-cord_2[1])**2))
print(distance)