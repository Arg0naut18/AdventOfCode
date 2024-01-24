limits = {
  # 12 red cubes, 13 green cubes, and 14 blue cubes
  "red": 12,
  "green": 13,
  "blue": 14
}

def parse_game(game_data):
  game_id, data = game_data.split(": ")
  game_id = int(game_id.split(" ")[1])
  games = data.split("; ")
  game_map = {}
  for game in games:
    coins = game.split(", ")
    for coin in coins:
      val, key = coin.split(" ")
      val = int(val)
      if key in game_map:
        game_map[key]+=val
        if game_map[key]>limits[key]:
          return -1, False
      else:
        if val>limits[key]:
          return -1, False
        game_map[key]=val
  print(game_map, limits)
  return game_id, True

def solution(is_trial: bool=False):
  summ = 0
  file_path = r'./trial_inputs.txt' if is_trial else r'./inputs.txt'
  with open(file_path, 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
      result = parse_game(line)
      if result[1]:
        print(result[0])
        summ+=result[0]
  return summ

if __name__ == "__main__":
  print(solution(is_trial = False))