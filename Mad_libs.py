"""Something."""
madLib_dic = {
    "noun": "blank",
    "verb": "blank",
    "adjective": "blank"
}

list = ["noun", "verb", "adjective"]
list2 = ["enter noun", "enter verb", "enter adjective"]
for x in range(len(list)):
    key = list[x]
    new_value = input(list2[x])
    madLib_dic[key] = new_value

response = f"This is a noun {madLib_dic['noun']}"
print(response)
