import uvicorn

if __name__ == "__main__":
    port = 8000
    uvicorn.run("FactsAPI:app", host="0.0.0.0",port=port,reload=True)
