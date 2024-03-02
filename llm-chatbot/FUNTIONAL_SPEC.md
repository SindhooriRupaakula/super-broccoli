# Functional spec for chatbot

### main()
* Description: Takes the inputs from user and directs them to the chatbot as prompts

### setupConnection()
* Inputs: Base prompt string
* Outputs: client
* Description: Gets the API key from env variables and creates the client object. This function also creates a base promt to provide context to the llm.

### send Request()
* Inputs: request prompt from the user
* Outputs: The response from the llm
* Description: Saves the request to the prompt list and sends the request. The reponse is then saved to the prompt list to keep adding to the context of the chat.

### savePrompt()
* Inputs: prompt string
* Outputs: N/A
* Description: Saves the prompt or response to the prompt list