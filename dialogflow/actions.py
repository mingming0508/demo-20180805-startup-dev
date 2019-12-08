import random
from django.template.loader import render_to_string
from .naver import 블로그_검색, 상한가_크롤링, 테마별_시세_크롤링
from .weather import get_weather_data, get_location

def save_location(text):
    print('-------------------------------------------------------')
    print(text)
    
    get_location(text)
    result = get_weather_data()
    
    t = f'현재 온도는 {result.get("T3H")}℃\n'
    t += f'오늘의 최고 온도는 {result.get("TMX")}℃\n'
    t += f'현재 습도는 {result.get("REH")}%\n'
    t += f'현재 강수 확류은 {result.get("POP")}%\n'
    t += f'현재 풍속은 {result.get("UUU")}m/s\n'
    print(t)
    return t
    
def search(search_engine, keyword):
    if search_engine == '네이버 블로그':
        post_list = 블로그_검색(keyword)
        speech = render_to_string('dialogflow/naver_blog_search_result.txt', {
            'post_list': post_list[:3],
        })
    else:
        speech = '{}는 지원하지 않습니다.'.format(search_engine)

    return {'speech': speech}
    


# def weather_search(weather):
#     print(weather)
#     if weather == '오늘의 날씨':
#         result = get_weather_data()
#         speech = result.get("TMN")
        
#     elif weather == '내일의 날씨':
#         speech = 내일날씨_크롤링()
    
#     else:
#         speech = '{}는 지원하지 않습니다.',format(weather)
    
#     return {'speech': speech}


def stock_search(stock_search_term):
    print("========================================")
    print(stock_search_term)
    if stock_search_term == '상한가 종목':
        speech = 상한가_크롤링()

    elif stock_search_term == '테마별 시세':
        speech = 테마별_시세_크롤링()

    else:
        speech = '{}는 지원하지 않습니다.'.format(stock_search_term)

    return {'speech': speech}

