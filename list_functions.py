lotto_nmbers = [4,8,16,32,64]
friends = ["jay","el","britannia","lelouch","schneizel"]

#friends.extend(lotto_nmbers) #Adding lists together

friends.append("Creed") #Adds item to end of list

friends.insert(1, "kay") #Adds item to specified index and pushes other items to incremental index

friends.remove("el") #removes item

friends.pop() #Removes last item

#friends.clear() #Clears list

print(friends.index("lelouch")) #returns index of element

print(friends.count("jay")) #Counts occurences of specified item

friends.sort()

lotto_nmbers.reverse()

print(lotto_nmbers)

print(friends)

friends2 = friends.copy()

print(friends2)