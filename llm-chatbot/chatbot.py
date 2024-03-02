from openai import OpenAI
from pprint import pprint

prompt_list = []

def setup_connection():
  """setup connection and system prompt for llm

  Returns:
      OpenAI: OpenAI cient object
  """
  client = OpenAI()
  prompt_list.append({
        "role": "system",
        "content": "You are a national swimming champion in India. Answer all questions as Uday the swimming champion.\n"
      })
  return client
  
def get_response(client, userStr):
  """get chat response from llm and maintain chat history

  Args:
      client (OpenAI): client object
      userStr (str): query string entered by user as input
  """
  prompt = {
        "role": "user",
        "content": userStr
      } 
  save_prompt(prompt)

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages= prompt_list,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0.6,
    presence_penalty=0.3,
    stop=["\nBot", "\nUser"]
  ) 
  
  print('Bot:', response.choices[0].message.content)
  
  save_prompt({
    "role": "assistant",
    "content": response.choices[0].message.content
  })

def save_prompt(prompt):
  """save all prompts from user and AI assistant to maintain chat history

  Args:
      prompt (dict{str: str}): prompts from user and AI asistant as dictionary                                                                     
  """
  prompt_list.append(prompt)

def main():
  """setup openai connection
     get input from user and query using openai api
  """
  while True: 
    prompt = input("\nUser: ")
    
    client = setup_connection()
    get_response(client, prompt)
    
    # enc chat if prompt ends with 'bye!'
    if(prompt.lower.endswith('bye!')):
      break;

if __name__ == "__main__":
  main()