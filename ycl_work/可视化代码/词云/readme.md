# read_file的功能
```
# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 9:00
# @Author  : 尹成林
# @Site    : https://me.csdn.net/sdyinruichao
# @File    : read_file.py
# @Software: PyCharm
```
# 主要工作内容
- 目录扫描返回文件名
- 找到新增文件
- 获得文件名后缀
- 根据不同文件名使用不同的读取方式
- 循环往复以上工作

# 实现方法
### 目录扫描
```python
def scan_files(directory, files_list, prefix=None, postfix=None):
    list = []
    for fpath, dirname, fnames in os.walk(directory):
        for i in fnames:
            if str(i) not in files_list:
                list.append(str(i))
                files_list.append(str(i))
    return list
```
### 返回文件名后缀

```python
# 加载文件后缀名
def get_file_type(filename):
    a = os.path.splitext(filename)[-1]
    return a.split('.')[1]
```
### 循环读取
```python
def test_read_file():
    list = []
    while True:
        time.sleep(1)
        ll = scan_files("data/Raw_data", list)
        print(ll)
        for i in ll:
            print(get_file_type(i))
```
# 可以修改的地方
- 循环可以通过爬虫脚本运行来控制，不一定需要time
- 和上一篇的可视化之间属于相互调用的关系，到时候后期整合要注意导入包可能存在冲突

