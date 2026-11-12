def show_menu():
    print("学生成绩管理系统")
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 查询学生")
    print("4. 统计平均分")
    print("5. 退出")
def main():
    students = []
    request=0
    while request!=5:
        show_menu()
        request=int(input('请选择功能：'))
        if request==1:
            print('添加学生功能开发中')
        elif request==2:
            print('删除学生功能开发中')
        elif request==3:
            print('查询学生功能开发中')
        elif request==4:
            print('平均分功能开发中')
        elif request==5:
            print("程序结束")
            break
        else:
            print('输入无效，请重新选择')
if __name__ == "__main__":
    main()