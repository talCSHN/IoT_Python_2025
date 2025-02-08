import os
from Student import Student

VERSION = 2.0

studentList = []


def clearScreen():
  command = 'clear'
  if os.name in ('nt', 'dos'):
    command = 'cls'

  os.system(command)


def selectNum():
  menu = (f'부경대학교 포털시스템 v{VERSION}\n'
          '1. 학생 정보 입력\n'
          '2. 학생 정보 출력\n'
          '3. 학생 정보 검색\n'
          '4. 학생 정보 삭제\n'
          '5. 앱 종료\n')
  print(menu)
  try:
    selectedNum = int(input('메뉴 번호 입력: '))
  except Exception as e:
    selectedNum = 0
  return selectedNum

def setStudent():
  name, age, major, degree = input('학생정보 입력[이름|나이|전공|학점 순] > ').split('|')
  age = int(age)
  degree = float(degree)
  student = Student(name=name, age=age, major=major, degree=degree)
  return student

def showStudent(items: list):
  for i in items:
    print(i)

def searchStudent(items: list, firstName: str):
  for i in items:
    if i.isNameContain(firstName):
      print(i)

def deleteStudent(items: list, name: str):
  for i, item in enumerate(items):
    if item.isNameExist(name):
      del items[i]

def saveStudent(items: list):
  f = open('student_db.txt', encoding='utf-8', mode='w')
  for i in items:
    f.write(f'{i.name}|')
    f.write(f'{i.age}|')
    f.write(f'{i.major}|')
    f.write(f'{i.degree}\n')

  f.close()

def loadDB(items: list):
  f = open('student_db.txt', encoding='utf-8', mode='r')
  while True:
    line = f.readline().replace('\n', '')
    if not line: break

    lines = line.split('|')
    name = lines[0]
    age = int(lines[1])
    major = lines[2]
    degree = float(lines[3])

    student = Student(name, age, major, degree)
    items.append(student)

  f.close()

def run():
  
  clearScreen()
  global studentList
  loadDB(studentList)
  while True:
    selectedNum = selectNum()
    if selectedNum == 1:
      student = setStudent()
      studentList.append(student)
    elif selectedNum == 2:
      print('학생 정보 보기')
      showStudent(studentList)
    elif selectedNum == 3:
      print('학생 검색')
      firstName = input('검색할 학생 이름 입력 > ')
      searchStudent(studentList, firstName)
    elif selectedNum == 4:
      print('학생 삭제')
      name = input('삭제할 학생 입력 > ')
      deleteStudent(studentList, name)
    elif selectedNum == 5:
      saveStudent(studentList)
      break
    else:
      pass

    input()
    clearScreen()
    
