import openai
openai.api_key = "your-api-key-here"

def get_gpt3_response(prompt):
    # Make a request to the OpenAI API for a response to the prompt
    response = openai.Completion.create(
        engine="gpt-4",  # You can also use "text-davinci-003" for GPT-3
        prompt=prompt,
        max_tokens=150,  # Limit the length of the response
        n=1,  # Number of responses to generate
        stop=None,  # You can specify stop sequences if needed
        temperature=0.7  # Controls randomness: 0.0 (more deterministic) to 1.0 (more creative)
    )
    
    # Extract and return the text response from the API response
    return response.choices[0].text.strip()


def chatbot():
    print("Chatbot (GPT-3/4) is ready to chat! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Get response from GPT-3/4
        response = get_gpt3_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chatbot()

conversation_history = []

def get_gpt3_response(prompt):
    conversation_history.append(f"You: {prompt}")
    full_prompt = "\n".join(conversation_history)
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=full_prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    answer = response.choices[0].text.strip()
    conversation_history.append(f"Chatbot: {answer}")
    return answer
