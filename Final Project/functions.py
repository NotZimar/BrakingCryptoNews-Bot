import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def Search_for_news():
    url = 'https://cryptopanic.com/api/free/v1/posts/?auth_token=f70a772eae16fc07edc5dd220d43ae69ef41df42&kind=news'
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        results = json_data.get("results", [])

        if not results:
            return None

        latest_news = results[0]
        title = latest_news.get("title", "عنوانی یافت نشد")
        url = latest_news.get("url", "لینکی یافت نشد")

        return {
            "title": title,
            "url": url
        }
    else:
        print(f"Error in API call: {response.status_code}")
        return None

def Translate(Text):
    response = requests.get(
        f'https://api.api4dev.ir/claude?question=این متنی که بهت میدم رو بدون هیچ چیز اضافه ای ترجمه کن و اصطلاحات یا اسم ها و برند هارو ترجمه نکن و برگردون : {Text}'
    )
    if response.status_code == 200:
        return response.text
    else:
        translator = Translator()
        result = translator.translate(Text, src='en', dest='fa')
        return result.text


def importance_rate(title):
    response = requests.get(
        f'https://api.api4dev.ir/claude?question=سلام به این خبری که بهت میدم نگاه کن از یک تا ده به اهمیت خبر نمره بده و نزولی یا صعودی بودش رو در صورت امکان بگو و چیز اضافه ای نگو: {title}'
    )
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "نمره‌ای یافت نشد"