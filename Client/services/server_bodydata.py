import requests
from Client.config import BASE_URL, API_TIMEOUT

class BodyDataService:
    @staticmethod
    def request_current_weight_save(user_id: int, current_weight:float):
        """向服务端发送有氧训练完成请求"""
        url = f"{BASE_URL}/body/weight/save_current_weight"
        data = {
            "user_id": user_id,
            "current_weight": current_weight
        }

        try:
            response = requests.post(url, json=data, timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"有氧完成请求失败：{e}")
            return None

