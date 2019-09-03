# Creating empty dictionary
mad_libs_dic = {}

list1 = ["Please enter a noun: ", "Please enter a verb: ", "Please enter a adjective: ", "Please enter an adverb: "]
# Empty list to populate with user response
list2 = []

# Looping through the list of prompts
for x in range(len(list1)):
    key = list1[x]
    user_input = input(list1[x])
    mad_libs_dic[key] = user_input
    # for letter in user_input:
    #     if letter == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0':
    #         print("Not valid response")
    #     else:
    # return letter

print_out_story = f"\033[0;33;40m A {mad_libs_dic['Please enter a noun: ']} is in the room. \033[0;32;40m The {mad_libs_dic['Please enter a noun: ']} {mad_libs_dic['Please enter a verb: ']} {mad_libs_dic['Please enter a adjective: ']}. \033[0;34;40m The {mad_libs_dic['Please enter a noun: ']} {mad_libs_dic['Please enter a verb: ']} {mad_libs_dic['Please enter an adverb: ']}. "
print(print_out_story)
