from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Valid title abbreviations

@app.get("/titled/{title}")
def get_players_info(title: str):

    url = f"https://api.chess.com/pub/titled/{title}"
    headers = {
        "User-Agent": "YourAppName/1.0"
    }
    response = requests.get(url, headers=headers)

    # Check for successful response
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data from Chess.com")

    data = response.json()
    return data

# Run the app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)