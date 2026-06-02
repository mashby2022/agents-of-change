import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Setup API Client
load_dotenv()
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

# 2. Define the model we are using today
# Note: Instructors can change this to nemotron, mixtral, etc.
MODEL = "meta/llama3-8b-instruct"

def main():
    """
    Workshop Exercise 1: 
    [Instructor will provide details here]
    """
    
    # Example prompt setup
    system_prompt = "You are a helpful AI assistant."
    user_prompt = "Hello!"

    # TODO: Write your API call here
    
    pass

if __name__ == "__main__":
    main()
