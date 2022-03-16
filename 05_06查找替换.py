hello_str = "hello world"

# 1.判断是否一指定字符串开始
print(hello_str.startswith("he"))

# 2.判断是否以指定字符串结束
print(hello_str.endswith("ld"))

# 3.查找指定字符串
# 类似于index 同样可以查找指定的字符串在大字符串中的索引
print(hello_str.find("lod"))
print(hello_str.index("lo"))
# find 如果找不到会返回-1
# index 找不到会报错

# 4.替换字符串
print(hello_str.replace("lo", "lllllo"))
print(hello_str)
# 替换字符串，只会修改字符串，并不会保存修改原有的字符串

