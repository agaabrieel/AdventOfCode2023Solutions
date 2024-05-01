
def parse_input(filepath: str) -> dict:
    
    parsed_data: dict[str, set] = {}
    
    file_buffer: str = ""
    with open(filepath, "r") as f:
        file_buffer = f.readlines()
        for line in file_buffer:
            colon_split_line: list[str] = line.split(":")
            game_id = colon_split_line[0].split(" ")[1]
            games = [game.lstrip() for game in colon_split_line[1].split(";")]
            parsed_data[game_id] = games
            
    return parsed_data

def find_impossible_games(games: dict[str, set], balls: dict[str, int]) -> list[str]:
    
    impossible_games: list[str] = []
    
    for game_id, games_set in games.items():
        for game in games_set:
            game_set = game.replace(",", "").split(" ")
            print(game_id, game_set)

parsed_data = parse_input("day_two_input.txt")
find_impossible_games(parsed_data, {"red": 12,
                                    "green": 13,
                                    "blue": 14})