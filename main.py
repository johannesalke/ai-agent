import os

from dotenv import load_dotenv # pyright: ignore[reportMissingImports]

from google import genai
from google.genai import types # pyright: ignore[reportMissingImports]
import argparse




def main():
    print("Hello from aiagent!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    print(args)
    # Now we can access `args.user_prompt`

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
    model='gemini-2.5-flash', contents=messages)
    

    metadata = response.usage_metadata
    if metadata == None:
        raise RuntimeError("Response metadata was null. Response invalid.")
    if args.verbose == True:
        print(f"User prompt: {args.user_prompt}\nPrompt tokens: {metadata.prompt_token_count}\nResponse tokens: {metadata.candidates_token_count}")
    
    

    print(response.text)



if __name__ == "__main__":
    main()
