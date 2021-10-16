s=input()  #getting input from user
s1=[i for i in s]  #creating the list for s to compare
l={}  #empty dict for storing the letters and count
l1=[]  #empty list
for i in range(len(s)): #iterating through the list
    l[s[i]]=s1.count(s[i])  #adding key,value pair to dict ,the value will be the count of each letter
max_key=max(l,key=(l.get))  #from the dict to get the most repeated character
all_values=l.values() 
val=max(all_values)  #To get highest count
for key,values in l.items(): 
    if values==val: # if any of the values from the list l is same as the highest count 
        l1.append(key)  #we append it to the list l
l3=[x for x in s1 if x in l1]  #To print all the repeated characters
print(*l3,sep="") #unpacking the list values