from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!'

### New Function
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
### End of new function

a = 10 
b = 4
@app.get('/add/{a}/{b}')
async def add(a: float, b: float):
    result = a + b
    return {"operation": "add", "a": a, "b": b, "result": result}