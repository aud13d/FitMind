import requests
from Client.config import BASE_URL, API_TIMEOUT

class BodyDataService:
    @staticmethod
    def request_get_latest_body_data(user_id):
        """向服务端发送有氧训练完成请求"""
        url = f"{BASE_URL}/body/get_latest_body_data"
        data = {
            "user_id": user_id
        }

        try:
            response = requests.post(url, json=data, timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"当前体重保存请求失败：{e}")
            return None

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
            print(f"当前体重保存请求失败：{e}")
            return None

    @staticmethod
    def request_target_weight_save(user_id:int, target_weight:float):
        """向服务端发送有氧训练完成请求"""
        url = f"{BASE_URL}/body/weight/save_target_weight"
        data = {
            "user_id": user_id,
            "target_weight": target_weight
        }
        try:
            response = requests.post(url, json=data,timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"目标体重保存请求失败：{e}")
            return None

    @staticmethod
    def request_current_body_fat_rate_save(user_id:int, body_fat_rate:float):
        """向服务端发送有氧训练完成请求"""
        url = f"{BASE_URL}/body/weight/save_current_body_fat_rate"
        data = {
            "user_id": user_id,
            "body_fat_rate": body_fat_rate
        }
        try:
            response = requests.post(url, json=data,timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"当前体脂率保存请求失败：{e}")
            return None

    @staticmethod
    def request_current_circumference_save(user_id:int, part:str, value:float):
        """向服务端发送有氧训练完成请求"""
        url = f"{BASE_URL}/body/circumference/save_current_circumference"
        data = {
            "user_id": user_id,
            "part": part,
            "value": value
        }
        try:
            response = requests.post(url, json=data,timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"当前身体围度保存请求失败：{e}")
            return None



