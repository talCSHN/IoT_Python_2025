# 모듈
class Movie:
    def __init__(self, title, year, company, rate):
        self.__title = title
        self.__year = year
        self.__company = company
        self.__rate = rate

    def __str__(self): # 문자열 포맷팅
        str_res = (f'제목: {self.__title}'
                   f'({self.__year})\n'
                   f'제작사: {self.__company}\n'
                   f'평점: {self.__rate}')
        return str_res
    
    # 찾는 이름이 포함 되어 있으면 True
    def isNameContain(self, name):
        if name in self.__title:    # name = '어벤져스', __title = '어벤져스 : 인피니티 워' | '어벤져스 : 엔드게임'
            return True
        else:
            return False
        
    # 찾는 이름이 완벽하게 일치하면 True
    def isNameExist(self, title):
        if self.__title == title:
            return True
        else:
            return False
        
    # 변수값 가져오기 getter 함수
    def getTitle(self):
        return self.__title
    
    def getYear(self):
        return self.__year
    
    def getCompany(self):
        return self.__company
    
    def getRate(self):
        return self.__rate
