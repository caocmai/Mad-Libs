madLib_dic = {}

list1 = ["Please enter a noun: ", "Please enter a verb: ", "Please enter a adjective: "]
list2 = []

for x in range(len(list1)):
    key = list1[x]
    new_value = input(list1[x])
    madLib_dic[key] = new_value

response = f"This is a noun {madLib_dic['Please enter a noun: ']}"
print(response)