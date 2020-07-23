
#this resets high score outside of the game

import json

with open("high_score.json", "w") as j_object: #we open json file where we store the highest score
    high_score = 0
    json.dump(high_score, j_object)