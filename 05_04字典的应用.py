
# 使用 多个键值对，存储 描述一个 物体的相关信息--描述更复杂的数据信息
#  将多个字典放在一个列表中，在进行遍历
card_list = [
    {"name": "wang",
     "age": "15",
     "number": "211231"},
    {"name": "yu",
     "age": "21",
     "number": "1231231"}
]

for card_info in card_list:
    print(card_info)