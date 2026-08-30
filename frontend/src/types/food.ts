export interface Food {
  id: number,
  name: string,
  calories_per_100g: number,
}

export interface FoodEntry {
  food: Food,
  quantity_g: number,
}
