# 클래스(Class)
class ClassName:
    pass    # pass 키워드를 사용해서 빈 클래스를 생성 할 수 있다.


""" 클래스(Class):
클래스(class)란 객체를 표현하기 위한 문법으로, 객체를 찍어내는 틀과 같다. 
객체(object)는 특정한 개념이나 모양으로 존재하는 것이며, 프로그래밍으로 클래스를 통해서 만들수 있다. 

파이썬에서처럼 클래스와 객체로 객체를 프로그래밍할는 것을 객체지향(object oriented)프로그래밍 이라 말한다.
(프로그래밍의 복잡한 문제를 잘게 나누어 객체로 만들고, 그러한 객체들을 조합해서 문제를 해결함)

클래스는 

class 클래스이름:
과 같이 만들며, 클래스이름의 규칙은 변수와 같다. (보통 클래스이름의 스타일로 맨앞은 대문자를 사용한다)
클래스 안에서는 속성(attribute)과 메쏘드(method)가 들어가는데, 각각 클래스안에서 쓰이는 변수와 함수다. 

클래스가 객체를 표현하는 문법, 형태이고, 클래스를 구현한 것이 객체라 했는데, 인스턴스(instance)라는 표현도 사용한다.
인스턴스는 객체와 같은 의미지만, 객체만 말할땐 객체라고 쓰고, 클래스랑 연관지어 말할 땐 인스턴스라 표현한다.


참고로 지금까지 배웠던 자료형(int, list, dict)으로 표현되는 값들은 모두 객체(자료형 클래스의 인스턴스)에 속한다.
그래서 자료형마다의 메쏘드가 있었고, 속성도 있었던 것이다. 
(type()함수로 인자값이 어떤 클래스인지 반환하는데, 자료형객체를 넣으면 자료형 클래스를 반환)

클래스를 통해서 인스턴스를 생성할 때는 
"""

temp = ClassName()    # 인스턴스 = 클래스() 식으로 인스턴스를 생성

print(isinstance(temp, ClassName))  # ininstance(인스턴스, 클래스)로 인스턴스가 클래스에 속하는지 반환값을 출력
"""
인스턴스이름 = 클래스이름()
과 같은 형식으로 인스턴스(객체)를 생성한다. 클래스는 개념을 표현(정의)하는 것 뿐이지, 실제로 클래스를 사용하려면
위같이 인스턴스를 생성해야한다.

참고로 특정 클래스의 인스턴스인지 확인하려면 isinstance() 함수를 이용해서 판별할 수 있다.
isinstance(인스턴스, 클래스)와 같이 인자값을 넘기면, 맞을때 True, 다른 클래스의 인스턴스면 False를 반환한다.
"""