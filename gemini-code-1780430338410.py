import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from the .env file
load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

if not NVIDIA_API_KEY or NVIDIA_API_KEY == "your-nv-api-key-here":
    print("❌ Error: Please set your NVIDIA_API_KEY in the .env file.")
    exit(1)

print("🔄 Testing connection to build.nvidia.com...")

# Initialize the client pointing to NVIDIA's OpenAI-compatible endpoint
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=NVIDIA_API_KEY
)

try:
    response = client.chat.completions.create(
        model="meta/llama3-8b-instruct",
        messages=[{"role": "user", "content": "Reply with only the words: 'Connection successful!'"}]
    )
    print("✅ Success! NVIDIA NIM responded with:")
    print(f"   \"{response.choices[0].message.content}\"")
except Exception as e:
    print("❌ Connection failed! Error details:")
    print(e)