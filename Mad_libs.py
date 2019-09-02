madLibs_dic = {}

list1 = ["Please enter a noun: ", "Please enter a verb: ", "Please enter a adjective: "]
list2 = []

for x in range(len(list1)):
    key = list1[x]
    new_value = input(list1[x])
    madLibs_dic[key] = new_value

print_out_story = f"A {madLibs_dic['Please enter a noun: ']} is in the room. The {madLibs_dic['Please enter a noun: ']} {madLibs_dic['Please enter a verb: ']} {madLibs_dic['Please enter a adjective: ']}. "
print(print_out_story)