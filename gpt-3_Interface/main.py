import openai
import keys

openai.api_key = keys.api_key

def chatbot_response(message):
  model_engine = "text-davinci-002"
  prompt = (f"{message}")

  completions = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
  )

  message = completions.choices[0].text
  return message.strip()

while True:
  message = input("You: ")
  response = chatbot_response(message)
  print("Assistant: ", response)