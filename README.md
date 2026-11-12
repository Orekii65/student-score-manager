# 学生成绩管理系统

一个使用 Python 实现的学生成绩管理练习项目，支持添加、查询、删除学生以及统计平均分。

## 功能

- 显示主菜单
- 添加学生姓名和成绩
- 按姓名查询学生
- 按姓名删除学生
- 统计所有学生的平均分
- 处理无效菜单输入
- 连续操作，输入 5 退出程序

## 技术点

- Python 函数
- 列表与字典
- `while` 循环
- `if / elif / else` 条件判断
- f-string 格式化输出
- Git 版本管理

## 项目结构

```text
student-score-manager/
├── main.py
├── README.md
└── .gitignore
```

## 运行方式

### 1. 创建虚拟环境

```powershell
python -m venv .venv
```

### 2. 运行程序

```powershell
.\.venv\Scripts\python.exe main.py
```

## 使用示例

```text
学生成绩管理系统
1. 添加学生
2. 删除学生
3. 查询学生
4. 统计平均分
5. 退出
请选择功能：1
请输入学生姓名：张三
请输入学生成绩：85
添加成功：张三，成绩：85.0
```

## 主要函数

| 函数 | 作用 |
|---|---|
| `show_menu()` | 显示主菜单 |
| `add_student(students)` | 添加学生 |
| `find_student(students, name)` | 按姓名查找学生 |
| `query_student(students)` | 查询并显示学生信息 |
| `delete_student(students)` | 删除指定学生 |
| `calculate_average(students)` | 计算平均分 |
| `main()` | 控制程序主循环 |

## 当前说明

当前版本的学生数据保存在程序内存中，程序退出后数据会被清空。

## 后续计划

- 使用 JSON 保存和读取学生数据
- 使用 pytest 编写自动化测试
- 增加修改学生功能
- 增加成绩排序功能
- 优化代码结构和输入校验

## 项目状态

核心功能已完成，并已通过手动功能测试。
