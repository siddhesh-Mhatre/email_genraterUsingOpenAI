import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = "menation your api key"

# Streamlit app
def main():
    st.title("Email Generation with OpenAI GPT-3.5-turbo")

    # User input for the chatbot prompt
    input_text = st.text_area("Enter your prompt for the email:", "Dear [Name],\n\n")

    if st.button("Generate Email"):
        # Generate a response using the GPT-3 model
        response = generate_email(input_text)

        # Display the generated email
        st.subheader("Generated Email:")
        st.write(response)

# Function to generate email using GPT-3
def generate_email(prompt):
    model_engine = "gpt-3.5-turbo-instruct"  # Use "text-davinci-003" for email generation

    # Generate a response using the GPT-3 model
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=300,  # Set the desired length of the response
        n=1,  # Number of completions to generate
        stop=None,  # Specify custom stop tokens if needed
    )

    return response.choices[0].text

if __name__ == "__main__":
    main()
