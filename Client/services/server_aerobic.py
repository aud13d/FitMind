import requests
from Client.config import BASE_URL, API_TIMEOUT

class AerobicService:
    @staticmethod
    def request_aerobic_complete(user_id: int, name: str, type_: str, really_time: float, target_time: int,
                               start_date: str, end_date: str, interval_reminder: int = None, items: list = None):
        """向服务端发送有氧训练完成请求"""
        url = f"{BASE_URL}/aerobic/complete"
        data = {
            "user_id": user_id,
            "name": name,
            "type": type_,
            "really_time": really_time,
            "target_time": target_time,
            "start_date": start_date,
            "end_date": end_date,
            "interval_reminder": interval_reminder,
            "items": items,
        }
        try:
            response = requests.post(url, json=data, timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"有氧完成请求失败：{e}")
            return None
