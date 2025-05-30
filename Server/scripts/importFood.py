import json
import asyncio
from tortoise import Tortoise
from Server.database.config import DATABASE_CONFIG
from Server.models.food import Food

# 只提取这几个营养素
TARGET_NUTRIENTS = {
    "Energy": "energy_kcal",
    "Protein": "protein_g",
    "Carbohydrate, by difference": "carbs_g",
    "Total lipid (fat)": "fat_g"
}

async def load_and_insert_foods():
    await Tortoise.init(config=DATABASE_CONFIG)
    await Tortoise.generate_schemas()

    with open("FoodData_Central_foundation_food_json_2025-04-24.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    food_list = data.get("FoundationFoods", [])
    count = 0

    for food in food_list:
        name = food.get("description", "").strip()
        if not name:
            continue

        nutrients = {v: None for v in TARGET_NUTRIENTS.values()}
        for item in food.get("foodNutrients", []):
            nutrient = item.get("nutrient", {})
            nname = nutrient.get("name")
            if nname in TARGET_NUTRIENTS:
                field = TARGET_NUTRIENTS[nname]
                nutrients[field] = item.get("amount")

        # 判断是否至少有一个字段不为空
        if any(value is not None for value in nutrients.values()):
            await Food.create(name=name, **nutrients)
            count += 1

    print(f"成功导入 {count} 条食物数据")
    await Tortoise.close_connections()

if __name__ == "__main__":
    asyncio.run(load_and_insert_foods())
