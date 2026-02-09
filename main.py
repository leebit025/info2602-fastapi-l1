from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)



@app.get('/stats')
async def get_stats():
    counts = {}
    for student in data:
        # Count programme
        programme = student['programme']
        if programme in counts:
            counts[programme] += 1
        else:
            counts[programme] = 1
        
        # Count preference
        pref = student['pref']
        if pref in counts:
            counts[pref] += 1
        else:
            counts[pref] = 1
    
    return counts
    
