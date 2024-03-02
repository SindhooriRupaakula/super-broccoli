from openai import OpenAI
from pprint import pprint

def chat(prompt):
  client = OpenAI()

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      #{"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.Compose a poem that explains the concept of recursion in programming."},
      {"role": "user", "content": prompt}
    ]
  )

  print(completion.choices[0].message)

def main():
    # setup openai connection
    #get input from user and query using openai api
    prompt = input("Enter prompt: ")
    chat(prompt)

if __name__ == "__main__":
  main()