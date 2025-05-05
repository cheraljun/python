git add lxf readme.md

git commit -m "更新readme.md"

git remote add origin git@github.com:cheraljun/python.git

git remote add origin https://github.com/cheraljun/python.git

git push origin master

# python日记

# 模块化代码。

# 问题：

# 多种格式化方式混用，逗号分隔（非格式化，仅用于拼接）用逗号分隔字符串和变量，输出有多余空格。

# f'{up:.1f}%'  本应嵌入字符串，却作为独立参数传递，逻辑混乱。

# 例子如下

```
print('debug...', '去年成绩', lyscore, '今年成绩', tyscore, '提升率', f'{up:.1f}%',)
```
