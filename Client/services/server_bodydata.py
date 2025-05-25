import requests
from Client.config import BASE_URL, API_TIMEOUT
from datetime import date

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

    @staticmethod
    def request_weight_history(user_id: int):
        """获取体重历史记录"""
        url = f"{BASE_URL}/body/weight/get_weight_history"
        data = {
            "user_id": user_id
        }

        try:
            response = requests.post(url, json=data, timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"体重历史记录请求失败：{e}")
            return None

    @staticmethod
    def request_body_fat_rate_history(user_id: int):
        """获取体脂率历史记录"""
        url = f"{BASE_URL}/body/weight/get_body_fat_rate_history"
        data = {
            "user_id": user_id
        }

        try:
            response = requests.post(url, json=data, timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"体脂率历史记录请求失败：{e}")
            return None

    @staticmethod
    def request_delete_weight_record(user_id:int,date):
        """删除体重记录"""
        url = f"{BASE_URL}/body/weight/delete_weight_by_date"
        data = {
            "user_id": user_id,
            "date": date.strftime("%Y-%m-%d")
        }
        try:
            response = requests.post(url, json=data,timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"删除体重记录请求失败：{e}")
            return None

    @staticmethod
    def request_delete_body_fat_rate_record(user_id:int,date):
        """删除体脂率记录"""
        url = f"{BASE_URL}/body/weight/delete_body_fat_rate_by_date"
        date = {
            "user_id": user_id,
            "date": date.strftime("%Y-%m-%d")
        }
        try:
            response = requests.post(url, json=date,timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"删除体脂率记录请求失败：{e}")
            return None

    @staticmethod
    def request_circumference_history(user_id:int,part:str):
        """获取身体围度历史记录"""
        url = f"{BASE_URL}/body/circumference/get_circumference_history"
        data = {
            "user_id": user_id,
            "part": part
        }
        try:
            response = requests.post(url, json=data,timeout=API_TIMEOUT)
            print("服务端返回内容：", response.text)
            return response
        except requests.exceptions.RequestException as e:
            print(f"身体围度历史记录请求失败：{e}")
            return None









