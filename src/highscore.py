import os

from .config import HIGHSCORE_FILE

def load_highscore():
    best_time = 0
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, 'r') as file:
            content = file.readlines()
            if content:
                best_time_str = content[0].split(":")[1].split("s")[0].strip()
                best_time = float(best_time_str)
    
    return best_time

def write_highscore(time, date):
    if time > load_highscore():
        with open(HIGHSCORE_FILE, 'w') as file:
            file.write(f"Best Time: {time}s - Date: {date}\n")
        return True
    
    return False
