import requests
from Client.config import BASE_URL, API_TIMEOUT


class TrainService:
    @staticmethod
    def request_train_finish(user_id: int, name: str, duration: float, start_date: str, end_date: str, actions: list[dict]):
        """向服务端发送训练完成请求"""
        url = f"{BASE_URL}/train/finish"
        data = {
            "user_id": user_id,
            "name": name,
            "duration": duration,
            "start_date": start_date,
            "end_date": end_date,
            "actions": actions
        }
        try:
            response = requests.post(url, json=data, timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"训练完成请求失败：{e}")
            return None
