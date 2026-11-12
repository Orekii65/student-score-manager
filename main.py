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


def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student
    return None


def query_student(students):
    name = input("请输入要查询的学生姓名：").strip()
    thestudent = find_student(students, name)

    if thestudent is None:
        print("未找到该学生")
    else:
        print(f"姓名：{thestudent['name']}")
        print(f"成绩：{thestudent['score']:.1f}")


def delete_student(students):
    name=input("请输入要删除的学生姓名：").strip()
    thestudent=find_student(students,name)
    if thestudent is None:
        print("未找到该学生，无法删除")
    else:
        students.remove(thestudent)
        print(f"删除成功：{name}")


def calculate_average(students):
    total=0
    if len(students)==0:
        return 0
    else:
        for student in students:
            total+=student["score"]
        average=total/len(students)
        return average
def main():
    students=[]
    while True:
        show_menu()
        request=input('请选择功能：')
        if request=='1':
            add_student(students)
        elif request=='2':
            delete_student(students)
        elif request == "3":
            query_student(students)
        elif request=='4':
            average=calculate_average(students)
            print(f"平均分:{average:.1f}")
        elif request=='5':
            print("程序结束")
            break
        else:
            print('输入无效，请重新选择')
if __name__ == "__main__":
    main()