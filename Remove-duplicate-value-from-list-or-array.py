def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
    
list = []
n = int(input("Number of Inputs in List: "))

for i in range(0,n):
  list.append(input())
print("Items in the List: ",list)

print("Updated Items: ",Remove(list))
