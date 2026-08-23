import sys
from pathlib import Path
import unittest

sys.path.append(str(Path(__file__).resolve().parent))
sys.path.append(str(Path(__file__).resolve().parent.parent))

from homework_10 import QuestRoom

class TestQuestRoom(unittest.TestCase):

    def setUp(self):
        """Підготовка: створюємо базовий об'єкт кімнати перед кожним тестом."""
        self.room = QuestRoom("Піратський острів", 3, 2)

    # --- 1. Тести конструктора ---
    def test_init_attributes(self):
        """Перевірка правиності ініціалізації всіх початкових атрибутів."""
        self.assertEqual(self.room.room_name, "Піратський острів")
        self.assertEqual(self.room.room_level, 3)
        self.assertEqual(self.room.room_limit, 2)
        self.assertEqual(self.room.room_players, [])
        self.assertEqual(self.room.status, "waiting")
        self.assertEqual(self.room.events_log, [])

    # --- 2. Додавання гравців (add_player) ---
    def test_add_player_success(self):
        """Успішне додавання одного гравця та перевірка запису в лог."""
        result = self.room.add_player("Олег")
        self.assertEqual(result, "Player Олег added!")
        self.assertIn("Олег", self.room.room_players)
        self.assertIn("Player Олег joined", self.room.show_log())

    def test_add_player_order(self):
        """Перевірка збереження правильного порядку гравців у списку."""
        self.room.add_player("Олег")
        self.room.add_player("Даша")
        self.assertEqual(self.room.room_players, ["Олег", "Даша"])

    def test_add_player_limit_exceeded(self):
        """Перевірка відмови у додаванні при досягненні ліміту кімнати."""
        self.room.add_player("Олег")
        self.room.add_player("Даша")
        # Ліміт 2 гравці, 3-й не повинен додатися
        result = self.room.add_player("Іван")
        self.assertEqual(result, "No free slots!")
        self.assertEqual(len(self.room.room_players), 2)

    # --- 3. Вилучення гравців (remove_player) ---
    def test_remove_player_success(self):
        """Успішне видалення гравця та запис події в лог."""
        self.room.add_player("Олег")
        result = self.room.remove_player("Олег")
        self.assertEqual(result, "Player Олег deleted!")
        self.assertNotIn("Олег", self.room.room_players)
        self.assertIn("Player Олег left", self.room.show_log())

    def test_remove_player_not_found(self):
        """Спроба видалення гравця, якого немає у списку."""
        self.room.add_player("Олег")
        result = self.room.remove_player("Максим")
        self.assertEqual(result, "Player not found!")

    def test_remove_player_from_empty_room(self):
        """Спроба видалення гравця з порожньої кімнати."""
        result = self.room.remove_player("Олег")
        self.assertEqual(result, "Player not found!")

    # --- 4. Перевірка заповненості (is_full, free_slots) ---
    def test_is_full_and_free_slots(self):
        """Динамічна перевірка заповненості та кількості вільних місць."""
        self.assertFalse(self.room.is_full())
        self.assertEqual(self.room.free_slots(), 2)

        self.room.add_player("Олег")
        self.assertFalse(self.room.is_full())
        self.assertEqual(self.room.free_slots(), 1)

        self.room.add_player("Даша")
        self.assertTrue(self.room.is_full())
        self.assertEqual(self.room.free_slots(), 0)

    # --- 5. Запуск квесту (start) ---
    def test_start_empty_room(self):
        """Спроба запуску квесту без гравців."""
        result = self.room.start()
        self.assertEqual(result, "Room is empty!")
        self.assertEqual(self.room.status, "waiting")

    def test_start_success(self):
        """Успішний запуск квесту з гравцями та зміна статусу на active."""
        self.room.add_player("Олег")
        result = self.room.start()
        self.assertIn("QuestRoom:", result)
        self.assertEqual(self.room.status, "active")
        self.assertIn("Quest started", self.room.show_log())

    # --- 6. Скидання кімнати (reset_room) ---
    def test_reset_room(self):
        """Скидання кімнати: очищення гравців, повернення статусу waiting та лог."""
        self.room.add_player("Олег")
        self.room.start()

        result = self.room.reset_room()
        self.assertEqual(result, "Room reset!")
        self.assertEqual(self.room.room_players, [])
        self.assertEqual(self.room.status, "waiting")
        self.assertIn("Room reset", self.room.show_log())

    # --- 7. Список гравців (players_list) ---
    def test_players_list(self):
        """Перевірка повернення списку гравців та повідомлення для порожньої кімнати."""
        self.assertEqual(self.room.players_list(), "No players in the room")
        self.room.add_player("Олег")
        self.assertEqual(self.room.players_list(), ["Олег"])

    # --- 8. Лог подій (show_log) ---
    def test_show_log_sequence(self):
        """Перевірка точної послідовності записів у логу подій."""
        self.room.add_player("Олег")
        self.room.start()
        self.room.reset_room()

        expected_log = [
            "Player Олег joined",
            "Quest started",
            "Room reset"
        ]
        self.assertEqual(self.room.show_log(), expected_log)

    # --- 9. Комбіновані сценарії ---
    def test_scenario_full_cycle(self):
        """Комплексний сценарій: заповнення, вилучення, додавання, запуск та скидання."""
        # 1. Заповнюємо до ліміту
        self.room.add_player("Олег")
        self.room.add_player("Даша")
        self.assertTrue(self.room.is_full())

        # 2. Пробуємо додати зайвого гравця
        self.assertEqual(self.room.add_player("Максим"), "No free slots!")

        # 3. Вилучаємо гравця та додаємо нового
        self.room.remove_player("Олег")
        self.assertFalse(self.room.is_full())
        self.room.add_player("Максим")

        # 4. Запускаємо та перевіряємо статус
        self.room.start()
        self.assertEqual(self.room.status, "active")

        # 5. Скидаємо кімнату
        self.room.reset_room()
        self.assertEqual(self.room.status, "waiting")
        self.assertEqual(self.room.room_players, [])


if __name__ == "__main__":
    unittest.main()