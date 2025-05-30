import requests
from Client.config import BASE_URL, API_TIMEOUT

class MealService:
    @staticmethod
    def request_search_food(keyword: str):
        """根据关键字搜索食物"""
        url = f"{BASE_URL}/meal/food/search_food"
        data = {
            "keyword": keyword
        }

        try:
            response = requests.post(url, json=data, timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"食物搜索请求失败：{e}")
            return None
