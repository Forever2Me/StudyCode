xiaoming_dict = {"name": "小明"}

# 1.取值
print(xiaoming_dict["name"])

# 2.增加/修改
xiaoming_dict["age"] = 18
xiaoming_dict["name"] = "fuckday"

# 3.删除
xiaoming_dict.pop("age")

print(xiaoming_dict)