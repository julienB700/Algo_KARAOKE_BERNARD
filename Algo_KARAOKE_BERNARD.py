class player: 
    def __init__(self,pseudo,scores={}):
        self.pseudo = pseudo
        self.scores = scores
    
    def add_song(self, song_id):
        self.songs.append(song_id)

    def add_score(self, song_id,score):
        if song_id not in self.scores or score > self.scores[song_id]:
            self.scores[song_id] = score

    def update_score(self, song_id, score):
        if score > 0 and (song_id not in self.scores or score > self.scores[song_id] and score >= 50):
            self.scores[song_id] = score

    def get_average_score(self):
        if not self.scores:
            return 0 
        return sum(self.scores.values()) / len(self.scores)
    
    def get_total_score(self):
        return sum(self.scores.values())

    def get_best_score(self):
        if not self.scores:
            return 0
        return min (self.scores.values())
    
    def get_worst_score(self):
        if not self.scores:
            return 0
        return min (self.scores.values())
    
class karaoke:
    def __init__(self):
        self.songs = []
        self.players = {}

    def add_song(self,name):
        song_id = len(self.songs)
        self.songs.append({"name": name, "id": song_id})
    
    def add_player(self,pseudo):
        if pseudo in self.players:
            return self.players[pseudo]
        player_id = len(self.players)
        self.players[pseudo] = {"id": player_id, "scores": {}}
        return player_id
    
    def update_score(self,player_id,song_id,score):
        if score > 0 and (song_id not in self.players[player_id]["scores"] or score > self.players[player_id]["scores"][song_id]) and score >=50:
            self.players[player_id]["scores"][song_id] = score

    def get_player_score(self,player_id):
        return self.players[player_id]["scores"]
    
    def get_song_scores(self,song_id):
        return {p: s.get(song_id,0) for p, s in self.players.items()}

karaoke = karaoke()
song_id_0 = karaoke.add_song ("Paradise")
song_id_1 = karaoke.add_song ("birds")
Player1 = player ("P1", {0:100,1:90})
Player2 = player ("P2") ## no score 


Player1.update_score(0,95)
Player2.update_score(0,90)

print(Player1.get_average_score)
print(Player1.get_total_score)
print(Player1.get_best_score)
print(Player1.get_worst_score)

print(Player2.get_average_score)
print(Player2.get_total_score)
print(Player2.get_best_score)
print(Player2.get_worst_score)
