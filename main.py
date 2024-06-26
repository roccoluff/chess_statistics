from fastapi import FastAPI, HTTPException, Response
import requests

app = FastAPI()

@app.get("/monthly/{monthly_pgn}")
def get_monthly_png(username: str, year: int, month: int):

    url = f"https://api.chess.com/pub/player/{username}/games/{year}/{month}/pgn"
    headers = {
        "User-Agent": "chess_statistics/0.1",
    }
    response = requests.get(url, headers=headers)

    # Check for successful response
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data from Chess.com")
    

    # This extracts and puts the response in a text format
    pgn_content = response.text

    filename = f"ChessCom_{username}_{year}_{str(month).zfill(2)}.pgn"

     # Create and return the response with appropriate headers
    return Response(
        content=pgn_content,
        media_type="application/x-chess-pgn",
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )

# Run the app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


