from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

models_to_test = [
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-pro",
    "gemini-1.5-pro"
]

for m in models_to_test:
    try:
        llm = ChatGoogleGenerativeAI(model=m)
        res = llm.invoke("Hi")
        print(f"SUCCESS: {m}")
        break  # We only need one working model
    except Exception as e:
        print(f"FAILED: {m} - {e}")
