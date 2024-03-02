# Functional spec for chatbot

### main()
* Description: Takes the inputs from user and directs them to the chatbot as prompts

### setup_connection()
* Outputs: client
* Description: Sets up the connection to the llm with the system prompt.

### get_response()
* Inputs: client, userstr
* Description: Gets the response from the AI assistant and parses it for the user. The prompts are saved using the save_prompt() method

### save_prompt()
* Inputs: prompt string
* Outputs: N/A
* Description: Saves the prompt or response to the prompt list