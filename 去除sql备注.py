'''
版权声明:下方代码为CSDN博主「maozexijr」的原创文章,本人遵循CC 4.0 BY-SA版权协议,转载附上原文出处链接及本声明。
原文链接:https://blog.csdn.net/MAOZEXIJR/article/details/88114901
'''

# 实现MySQL脚本文件的读取,包含了对备注内容的处理。
# 入参path 是脚本文件的绝对路径，出参为 SQL语句的字符串列表
def readSqlFile(path):
    f = open(path, "r", encoding="UTF-8")
    lines = f.readlines()

    sqlList = []
    thisSql = ""
    mulNote = False
    for line in lines:
        string = str(line).strip()
        if string == "":
            continue

        # part1 multi-line comment
        if mulNote:
            if string.startswith("*/"):
                mulNote = False
            continue
        if string.startswith("/*"):
            mulNote = True
            continue
        if string.startswith("#") or string.startswith("--"):
            continue

        strIn1 = False
        strIn2 = False
        for i in range(len(string)):
            c = string[i]
            # part2 string in sql
            if "'" == c:
                if not strIn1:
                    strIn1 = True
                else:
                    strIn1 = False
                continue

            if '"' == c:
                if not strIn2:
                    strIn2 = True
                else:
                    strIn2 = False
                continue

            if strIn1 is True and strIn2:
                continue

            # part3 end of sql
            if ";" == c:
                string = string[0:(i + 1)]
                break

            # part4 comment behind of the sql
            if "#" == c:
                string = string[0:i]
                break
            if "-" == c and i <= len(string) - 2 \
                    and "-" == string[i + 1]:
                string = string[0:i]
                break

        # part5 join multi-line for one sql
        thisSql += " " + string

        # part6 end of sql
        if string.endswith(";"):
            sqlList.append(copy.deepcopy(thisSql))
            thisSql = ""

    return sqlList
