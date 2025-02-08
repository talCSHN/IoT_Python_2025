class Student:
    # 생성자
    def __init__(self, name, age, major, degree):
        self.__name = name
        self.__age = age
        self.__major = major
        self.__degree = degree

    # toString
    def __str__(self):
        str_res = (f'이름: {self.__name} '
                   f'나이: {self.__age} '
                   f'전공: {self.__major} '
                   f'학점: {self.__degree}')
        return str_res
    
    def isNameContain(self, firstName):
        if firstName in self.__name:
            return True
        else:
            return False

    def isNameExist(self, name):
        if self.__name == name:
            return True
        else:
            return False
    
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @property
    def major(self):
        return self.__major
    
    @property
    def degree(self):
        return self.__degree
    
    @name.setter
    def name(self, new_name):

        if not type(new_name) == str:
            raise ValueError("이름을 문자로 입력하세요.")

        self.__name = new_name
        return self.__name
    
    @age.setter
    def age(self, new_age):

        if not isinstance(new_age, int):
            raise ValueError("나이를 숫자로 입력하세요.")

        self.__age = new_age
        return self.__age
    
    @major.setter
    def major(self, new_major):

        if not type(new_major) == str:
            raise ValueError("전공을 문자로 입력하세요.")
        
        self.__major = new_major
        return self.__major
    
    @degree.setter
    def degree(self, new_degree):

        if not isinstance(new_degree, float):
            raise ValueError("학점을 숫자로 입력하세요.")

        self.__degree = new_degree
        return self.__degree