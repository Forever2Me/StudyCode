xiaoming_dict = {"name": "小明",
                 "age": 16,
                 "size":111}

# 1.统计键值对数量
print(len(xiaoming_dict))

# 2.合并字典
temp_dict = {"height": 1.75}
# 如果被合并的字典存在已有的键值对，会覆盖原有的键值对

xiaoming_dict.update(temp_dict)

# 3、清空字典
# xiaoming_dict.clear()

# 4、删除指定键值对
xiaoming_dict.pop("age")

# 5.删除随机一个键值对
xiaoming_dict.popitem()
print(xiaoming_dict)
