import os
import re

# Mapping for ranks and suits
RANK_MAP = {
    "ace": "A", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6",
    "7": "7", "8": "8", "9": "9", "10": "10", "jack": "J", "queen": "Q", "king": "K"
}

SUIT_MAP = {
    "clubs": "C", "diamonds": "D", "hearts": "H", "spades": "S"
}

# Regex to capture rank, suit, and optional trailing duplicates (e.g., -1)
card_pattern = re.compile(
    r"English_pattern_(?P<rank>\w+)_of_(?P<suit>\w+)\.svg(?P<extra>-\d+)?\.png"
)

def rename_cards(directory="."):
    for filename in os.listdir(directory):
        match = card_pattern.match(filename)
        if match:
            gd = match.groupdict()
            rank = RANK_MAP.get(gd["rank"].lower())
            suit = SUIT_MAP.get(gd["suit"].lower())
            extra = gd["extra"] if gd["extra"] else "" # Preserves -1, -2 suffixes
            
            if rank and suit:
                new_name = f"{rank}{suit}{extra}.png"
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_name)
                
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_name}")
        else:
            if "placeholder" in filename:
                print(f"Skipped placeholder: {filename}")

if __name__ == "__main__":
    # Runs in the current working directory
    rename_cards()