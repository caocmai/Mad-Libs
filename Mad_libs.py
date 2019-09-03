# Creating empty dictionary
mad_libs_dic = {}

list1 = ["Please enter a noun: ", "Please enter a verb: ", "Please enter a adjective: "]
# Empty list to populate with user response
list2 = []

# Looping through the list of prompts
for x in range(len(list1)):
    key = list1[x]
    user_input = input(list1[x])
    mad_libs_dic[key] = user_input

print_out_story = f"A {mad_libs_dic['Please enter a noun: ']} is in the room. The {mad_libs_dic['Please enter a noun: ']} {mad_libs_dic['Please enter a verb: ']} {mad_libs_dic['Please enter a adjective: ']}. "
print(print_out_story)