# 1.Write a program to concatinate given list Solve it using two method, listA=[1,2,3,4,5] listB=["A","B","C","D"]?
listA=[1,2,3,4,5] 
listB=["A","B","C","D"]
result=(listA+listB)
listA.extend(listB)
print(result)    #  OUTPUT:[1, 2, 3, 4, 5, 'A', 'B', 'C', 'D']
print(listA)      #  OUTPUT:[1, 2, 3, 4, 5, 'A', 'B', 'C', 'D']

#2. Write a Program To Add strring "krishna"  in a empty list[] using method?
str=[]
str.append("krishna")
print(str)    #OUTPUT : ['krishna']

#3. Write a program to reverse a list =["A","B","C","D"]
list=["A","B","C","D"]
list.reverse() # OUTPUT : ['D', 'C', 'B', 'A']
print(list)

#4. Write a program to extend a empty list [] using another list = [""]
list = []
list.extend(['\u03B1','\u03B2','\u03B3'])
print(list)   #OUTPUT=['α', 'β', 'γ']

