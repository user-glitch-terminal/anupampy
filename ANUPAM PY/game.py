import random
import csv

# Load some game data (e.g., power-ups, enemies) from CSV
data_file = "game_data.csv"

# Example CSV format:
# type,name,value
# powerup,SpeedBoost,2
# enemy,Goblin,5
game_data = []
with open(data_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        game_data.append(row)

# Game world setup
WIDTH, HEIGHT = 10, 10
player = {"x": 5, "y": 5, "score": 0}

# Randomly place objects from data
objects = []
for item in game_data:
    obj = {
        "type": item["type"],
        "name": item["name"],
        "value": int(item["value"]),
        "x": random.randint(0, WIDTH-1),
        "y": random.randint(0, HEIGHT-1)
    }
    objects.append(obj)

def show_world():
    print(f"\nPlayer at ({player['x']},{player['y']}), Score: {player['score']}")
    for obj in objects:
        if obj["x"] == player["x"] and obj["y"] == player["y"]:
            print(f"You found a {obj['type']} - {obj['name']} (+{obj['value']})")
            handle_object(obj)

def handle_object(obj):
    if obj["type"] == "powerup":
        player["score"] += obj["value"]
    elif obj["type"] == "enemy":
        player["score"] -= obj["value"]
    objects.remove(obj)

def move_player(direction):
    if direction == "up" and player["y"] > 0:
        player["y"] -= 1
    elif direction == "down" and player["y"] < HEIGHT-1:
        player["y"] += 1
    elif direction == "left" and player["x"] > 0:
        player["x"] -= 1
    elif direction == "right" and player["x"] < WIDTH-1:
        player["x"] += 1
    else:
        print("Can't move that way!")

# Main game loop
print("Welcome to TextCy.io!")
while True:
    show_world()
    move = input("Move (up/down/left/right) or 'quit': ").lower()
    if move == "quit":
        break
    move_player(move)
print(f"Game Over! Final Score: {player['score']}")
