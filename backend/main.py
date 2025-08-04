from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from classes import Item

app = FastAPI()

origins = [
    "http://localhost:3000",   # your React dev server
    # "https://your-production-domain.com",
]

# 2️⃣ Add the CORS middleware *before* you include any routes:
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # or ["*"] for quick testing
    allow_credentials=True,         # allows cookies, Authorization headers, etc.
    allow_methods=["*"],            # GET, POST, PUT, OPTIONS, DELETE…
    allow_headers=["*"],            # also expose non-simple headers
)


@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Item:
    return item

