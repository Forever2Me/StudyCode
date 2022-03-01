xiaoming_dict = {"name": "小明",
                 "age": "16"}

# 1.统计键值对数量
print(len(xiaoming_dict))

# 2.合并字典
temp_dict = {"height": 1.75}


xiaoming_dict.update(temp_dict)
print(xiaoming_dict)
print(xiaoming_dict["age"])