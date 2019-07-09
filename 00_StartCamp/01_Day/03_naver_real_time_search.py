import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
names = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k')
#select는 리턴을 리스트로 해준다. 실시간검색어를 꺼내오는것이므로 select를 썼다. select_one을 쓴게아니라.
#print(type(names))

for idx, name in enumerate(names): #enumerate()에 리스트를 넣으면 리스트요소를 하나씩 뺄때 인덱스도 같이 뱉어준다.
    print(f'{idx+1}위: {name.text}')

