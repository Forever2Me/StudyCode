
poem_str = "\n静夜思\t李白\t床前明月光\t，\n疑是地上霜\t\t。举头望明月\n\n，低头思故乡。"

print(poem_str)
# 1、去除空白字符，拆分字符串
poem_list = poem_str.split()
print(poem_list)
# 2、合并字符串
result = " ".join(poem_list)
print(result)
