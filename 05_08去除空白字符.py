
poem = ["\n静夜思",
        "李白\t",
        "床前明月光，",
        "疑是地上霜。",
        "举头望明月，",
        "低头思故乡。"]

for poem_str in poem:
        # 1、先试用strip方法去除字符串中的空白字符
        # 2、在使用center方法居中显示文本

        print("|%s|" % poem_str.strip().center(10, "　"))