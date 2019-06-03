"""
크롤러 만들기
파일 다루기
"""
"""
1. 어느 웹 페이지에서 자료를 수집할 것이냐?
    - 내가 지금 보고 있는 웹 사이트의 주소
    - https://www.naver.com/
2. 해당 웹 페이지에서 어떤 html태그를 찾을 것이냐?
    - html이 어떻게 구성되어 있느냐?
    - html에서 어떻게 태그를 찾을 것이냐?
    
    - 실시간 급등 검색어가 들어있는 태그
    
3. 찾은 태그에서 원하는 데이터를 추출
    - text
      해당 태그안에 있는 검색어
    - url
    - image
"""
# 1. 자료가 있는 웹 페이지에 접속
# - requests : urllib의 랩핑 클래스
# pip install requests
# 2. 접속해서 얻어온 페이지 데이터를 html로 변환
# 3. html에서 요소 찾기
# 4. 찾은 요소에서 원하는 데이터 추출하기
# - BeautifulSoup
# pip install beautifulsoup4
import requests
url = "https://www.naver.com/"
# 데이터를 받아왔다.
req = requests.get(url)
# requests.post(url)

# 제대로 받아왔느냐? 확인
if req.status_code != requests.codes.ok:
    print("서버 응답 오류")
    exit()

# 받아온 데이터를 해석
# print(req.text)
# 문자를 -> 숫자로 데이터 타입 변경, 형변환(Type Casting)
# 어떤 형식의 데이터를 다른 형식의 데이터로 해석 Parsing
from bs4 import BeautifulSoup
html = BeautifulSoup(req.text, 'html.parser')

# html에서 원하는 요소를 찾아주는 함수
#html.select() # 요소를 전부다 찾아준다.
#html.select_one() # 찾은 요소 중에서 제일 먼저 나오는 요소 하나만 반환한다.
links = html.select('.PM_CL_realtimeKeyword_list_base .ah_a')

f = open('naver.txt','w',encoding='utf-8')
for link in links:
    rank = link.select_one('.ah_r').text
    keyword = link.select_one('.ah_k').text
    url = link.attrs['href']
    print(rank, keyword, url, file=f)

f.close()

"""
http method : 
get : 거의 대부분의 웹 사이트에 url을 입력한 링크를 클릭했을 때
      웹 페이지를 띄우려고
post : 웹 서버에 데이터를 전달하고 싶어서.
        회원 가입, 로그인, 글쓰기
"""



"""
1) 컨테이너 태그 : 다른 태그나 내용을 포함할 수 있어서
<p>
    내용
</p>
2) 엠티 태그 : 비디오나 이미지 등 단독으로 무언가를 표현하는 태그
<img src="이미지파일주소">

<태그이름 속성="속성값" 속성="속성값">
"""

"""
<태그이름 id="myname" class="names user" 속성="속성값" 속성="속성값">
1. 태그이름 : span p div a
2. id : 한 문서(한 페이지) 유니크 값, 태그의 주민번호
3. class : css 스타일을 적용하려고, 그룹 명, 별명, 한 태그가 여러개의 클래스를 갖을 수 있다.
4. 속성값 : id, class를 제외한 나머지
- <a href="주소">
- <img src="이미지주소">
- <div data-rel="">
"""

"""
selector 만들기
<span id='ah_k_1' class="ah_k" queryid="C1559365515554696285">벤자민 버튼의 시간은 거꾸로 간다</span>
<span class="ah_k key" queryid="C1559365516295246445">강식당2 재방송</span>
html.select("셀렉터값")

단일 셀렉터
tag : span
id : #ah_k_1
class : .ah_k

복합 셀렉터
1. ~이고 ~인것
span.ah_k.key
span#ah_k_1

2. ~안에 ~인것
.ah_a > .ah_k : 중간 경로 생략 불가능
.ah_a .ah_k : 중간 경로 생략 가능

"""








