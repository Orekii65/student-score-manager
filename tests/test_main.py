from main import calculate_average,find_student

def test_empty_average():
    result=calculate_average([])
    assert result==0

def test_average_two_student():
    students=[
        {'name':'张三','score':80},
        {'name':'李四','score':90}
    ]
    result=calculate_average(students)
    assert result==85

def test_average_one_student():
    student=[{'name':'张三','score':88}]
    result=calculate_average(student)
    assert result==88

def test_find_student_found():
    students=[
        {'name':'张三','score':80},
        {'name':'李四','score':90}
    ]
    result=find_student(students,'李四')
    assert result is not None
    assert result['name']=='李四'
    assert result['score']==90

def test_find_student_not_found():
    students=[
        {'name':'张三','score':80},
    ]
    result=find_student(students,'李四')
    assert result is None