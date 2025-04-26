import asyncio      # Import asyncio to run asynchronous code
import httpx        # Import httpx, an async HTTP client

# Sentences to send to the API
sentences = [
    "Saya suka makan nasi goreng.",
    "Hari ini cuaca sangat panas.",
    "Anjing itu sangat lucu.",
    "Kami akan pergi ke pantai besok.",
    "Apakah kamu punya hobi?",
    "Buku ini sangat menarik untuk dibaca.",
    "Sekarang waktunya istirahat.",
    "Kucing itu tidur di bawah meja.",
    "Makanan favorit saya adalah rendang.",
    "Kami berencana untuk berlibur ke Bali.",
]

# The URL of the API endpoint to which the sentences will be sent
api_url = "http://api:6000/predict"

# Send each sentence to the API and print the response
async def main():
    for sentence in sentences:
        try:
            async with httpx.AsyncClient() as aclient:
                response = await aclient.post(api_url, params={"text": sentence})
                response.raise_for_status()
                print(response.json())
        except Exception as e:
            print(e)
            continue

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())