class UserBodyData:
    current_weight = None
    current_weight_date = None

    target_weight = None

    body_fat_rate = None
    body_fat_rate_date = None

    circumferences = {}

    @classmethod
    def update(cls, data: dict = None, current_weight: float = None, target_weight: float = None,
               current_body_fat_rate: float = None):
        data = data or {}

        # 更新 current_weight
        if current_weight is not None:
            cls.current_weight = current_weight
            cls.current_weight_date = None
        elif "current_weight" in data:
            cw = data.get("current_weight")
            if isinstance(cw, dict):
                cls.current_weight = cw.get("value")
                cls.current_weight_date = cw.get("date")
            else:
                cls.current_weight = cw
                cls.current_weight_date = None

        # 更新 target_weight
        if target_weight is not None:
            cls.target_weight = target_weight
        elif "target_weight" in data:
            cls.target_weight = data.get("target_weight")

        # 更新 body_fat_rate
        if current_body_fat_rate is not None:
            cls.body_fat_rate = current_body_fat_rate
            cls.body_fat_rate_date = None
        elif "body_fat_rate" in data:
            bfr = data.get("body_fat_rate")
            if isinstance(bfr, dict):
                cls.body_fat_rate = bfr.get("value")
                cls.body_fat_rate_date = bfr.get("date")
            else:
                cls.body_fat_rate = bfr
                cls.body_fat_rate_date = None

        # 更新围度信息（circumference）
        if "circumference" in data:
            cls.circumferences = data["circumference"]

    @classmethod
    def clear(cls):
        cls.current_weight = None
        cls.target_weight = None
        cls.body_fat_rate = None
        cls.circumferences = {}

    @classmethod
    def get_circumference(cls, part):
        return cls.circumferences.get(part)
