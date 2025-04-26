from fastapi import FastAPI     # Import FastAPI
import hashlib                  # Import hashlib for generating MD5 hash

# Create FastAPI app
app = FastAPI()

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "API is healthy"}

# Predict endpoint
@app.post("/predict")
async def predict(text: str) -> int:
    # Hash text and map it to 0–3
    hashed = int(hashlib.md5(text.encode()).hexdigest(), 16)
    result = hashed % 4
    return result

# Run with Uvicorn if executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6000)
