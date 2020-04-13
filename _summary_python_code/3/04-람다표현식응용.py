proto_li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(map(lambda x: x+1, proto_li))
print(a)
""" 람다표현식응용:
map 함수의 인자로 람다 표현식을 사용한다면, 
map 함수 자체가 두번째 인자값으로 받은 반복가능한 객체를 
첫번째 인자값의 형식으로 각각의 요소들을 변환해서 map 객체로 반환하는데, (2폴터 1 참고)

첫번째 인자값으로 람다 표현식을 사용한다면, 인자값으로 전달받은 리스트의 요소하나하나를 각각 람다표현식으로 변환할 수 있다.

그리고 2>1에서 배웠듯이 map 함수에 변환할 값(반복가능한 객체)를 여러개 넣을 수도 있다. (주로 람다 표현식과 응용한다.)
"""

i = list(map(lambda x: "박수" if x % 3 == 0 else x, proto_li))
# 각각의 요소들을 람다표현식으로 변환하는데, 람다표현식에서 조건식을 넣어서 3의 배수면 '박수' 아니면 숫자를 출력
print(i)
"""
람다 표현식에서 조건문을 넣을 수 있다. 파이썬의 삼항연산자를 이용한다.
물론 삼항연산자를 중복해서도 사용할 수 있지만, 원만해선 가독성이 별로라서 안쓴다.
"""

i = list(filter(lambda x: x % 3 == 0, range(1, 21)))
print(i)
"""
filter 함수와 응용할 수 있다. filter(함수, 반복가능한 객체)는 map()함수와 비슷한데,
필터라는 이름대로 첫번째인자에서 함수의 반환값이 True 일때(반환 조건을 만족하는 요소)에 속하는 요소들만 묶어서 filter 객체로 반환한다.
반복하는 객체중에서 조건에 만족하는 요소들만 가져오고, 만족하지 않는 요소들은 걸러내는 함수다.

여기서 함수 인자에 람다 표현식을 사용할 수 있으며, 마찬가지로 람다 표현식의 반환 값에 만족하는 요소만 가져와서 filter 객체로 반환한다.
"""

l = [1, 2, 3, 4]
from functools import reduce   # 파이썬 3부터는 reduce 는 내장함수가 아니라서, functools 모듈에서 가져와야 된다.
print(reduce(lambda x, y: x*y, l))
"""
reduce 함수와도 응용할 수 있다. reduce(함수, 반복가능한 객체)는 얼핏 다른 함수와도 비슷한데, 
반복가능한 객체의 모든 요소를 첫번째 인자로 받는 함수의 매개변수들로 대입해서, 결국 모든 요소를 매개변수로 넣었을 때 누적되는 값을 반환한다.

ex) reduce(lambda x, y: x+y, [1, 2, 3,]) 같은 경우에선
[1, 2, 3]을 lambad x, y로 받아서 x+y로 반환하니까 ,
(1 + 2)+ 3 의 결과가 된다. (반복문 처럼 반복가능한 객체의 모든 요소를 누적 할 때 까지 반복한다.)
추가로 세번째 인자값으로 누적되는 값의 초깃값을 지정할 수 있다. (기본값은 0)

(솔직히 반복문으로 나타내는것이 보기에 좋다)
"""

# 팩트는.
# map, filter와 람다표현식을 응용 하는 것보다, 리스트 내포(표현식)을 응욯하는 것이 더 빠르고, 가독성도 좋다(상위호환)
# 그리고 reduce 보다 for, while 반복문을 응용하는 것이 가독성에 좋다,(reduce 함수는 복잡해지기만 해도 가독성이 맣이 떨어진다)
