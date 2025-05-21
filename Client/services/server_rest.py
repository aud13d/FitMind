import requests
from Client.config import *


class RestService:
    @staticmethod
    def request_rest_save(user_id: int, title: str, date: str, color: str):
        """向服务端发送休息保存请求"""
        url = f"{BASE_URL}/rest/save"
        data = {
            "user_id": user_id,
            "title": title,
            "date": date,
            "color": color
        }
        try:
            response = requests.post(url, json=data, timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"休息保存请求失败：{e}")
            return None