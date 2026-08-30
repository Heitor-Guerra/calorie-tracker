import type {User} from "./user"
import type {FoodEntry} from "./food"

export interface DailyLog {
  id: number,
  user: User,
  date: Date,
  entries: FoodEntry[]
}
