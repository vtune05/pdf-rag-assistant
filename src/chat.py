from dotenv import load_dotenv
load_dotenv()

from google import genai
client = genai.Client()

print("Write question\n")

while True:
    prompt = input("Your question: ")
    if prompt.lower() == "exit" :
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    print("Gemini:", response.text, "\n")