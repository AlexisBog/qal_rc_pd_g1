class QuestRoom:    
    def __init__(self, name, level, limit):
        self.room_name = name
        self.room_level = level
        self.room_limit = limit
        self.room_players = []
        self.status = "waiting"
        self.events_log = []

    def add_player(self, name):
        if len(self.room_players) >= self.room_limit:
            return "No free slots!"
        else:
            self.room_players.append(name)
            self.events_log.append(f"Player {name} joined")
            return f"Player {name} added!"

    def __str__(self):
        return (
            f"Room name - {self.room_name}\n"
            f"Level - {self.room_level}\n"
            f"Limit players - {self.room_limit}\n"
            f"Total players - {len(self.room_players)}"
        )
    def start(self):
        if not self.room_players:
            return f"Room is empty!"
        else:
            self.status = "active"
            self.events_log.append("Quest started")
            return f"QuestRoom: {self.room_name} | Difficulty: {self.room_level} | Players: {len(self.room_players)}/{self.room_limit}"

    def remove_player(self, name_pl):
        if name_pl in self.room_players:
            self.room_players.remove(name_pl)
            self.events_log.append(f"Player {name_pl} left")
            return f"Player {name_pl} deleted!"
        else:
            return "Player not found!"

    def is_full(self):
        return len(self.room_players) == self.room_limit

    def free_slots(self):
        return self.room_limit - len(self.room_players)

    def reset_room(self):
        self.status = "finished"
        self.room_players.clear()
        self.events_log.append("Room reset")
        self.status = "waiting"
        return "Room reset!"

    def players_list(self):
        if not self.room_players:
            return "No players in the room"
        else:
            return self.room_players

    def show_log(self):
        return self.events_log
    