def show_menu():
    print("学生成绩管理系统")
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 查询学生")
    print("4. 统计平均分")
    print("5. 退出")
def add_student(students):
    student={}
    student["name"]=input('请输入学生姓名:')
    student['score']=float(input('请输入学生成绩:'))
    students.append(student)
print(f"添加成功:{student['name']},成绩:{student['score']:.1f}")
def main():
    students=[]
    request=0
    while True:
        show_menu()
        request=input('请选择功能：')
        if request=='1':
            add_student(students)
        elif request=='2':
            print('删除学生功能开发中')
        elif request=='3':
            print('查询学生功能开发中')
        elif request=='4':
            print('平均分功能开发中')
        elif request=='5':
            print("程序结束")
            break
        else:
            print('输入无效，请重新选择')
if __name__ == "__main__":
    main()