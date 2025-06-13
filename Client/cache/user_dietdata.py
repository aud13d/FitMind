from datetime import datetime, date


class UserDietData:
    total_energy = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0
    total_drinks = 0.0

    meals = []  # 每餐数据（Meal的简化版）
    last_update_date: date = date.today()

    @classmethod
    def update(cls, meal_data: dict):
        """添加一餐，并更新当日总计"""
        # 检查并重置当日总计
        cls._check_reset()

        # 将餐数据添加到meals列表中
        cls.meals.append(meal_data)
        # 更新当日总能量
        cls.total_energy += meal_data.get("energy", 0.0)
        # 更新当日总蛋白质
        cls.total_protein += meal_data.get("protein", 0.0)
        # 更新当日总碳水化合物
        cls.total_carbs += meal_data.get("carbs", 0.0)
        # 更新当日总脂肪
        cls.total_fat += meal_data.get("fat", 0.0)
        # 更新当日总饮料
        cls.total_drinks += meal_data.get("drinks", 0.0)

    @classmethod
    def get_summary(cls):
        """返回当前总计（四舍五入取整）"""
        cls._check_reset()
        return {
            "energy": round(cls.total_energy),
            "protein": round(cls.total_protein),
            "carbs": round(cls.total_carbs),
            "fat": round(cls.total_fat),
            "drinks": round(cls.total_drinks)
        }

    @classmethod
    def clear(cls):
        cls.total_energy = 0.0
        cls.total_protein = 0.0
        cls.total_carbs = 0.0
        cls.total_fat = 0.0
        cls.total_drinks = 0.0
        cls.meals = []
        cls.last_update_date = date.today()

    @classmethod
    def _check_reset(cls):
        """如果跨天了就清空数据"""
        if cls.last_update_date != date.today():
            cls.clear()
