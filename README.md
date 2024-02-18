 
---

# How to Use Email Generation App with OpenAI GPT-3.5-turbo

This guide explains how to use the Streamlit app for generating emails with the OpenAI GPT-3.5-turbo model. Follow the steps below to get started:

## Prerequisites

1. Make sure you have Python installed on your system.

2. Install the required Python packages by running the following command in your terminal:

    ```bash
    pip install streamlit openai
    ```

3. Obtain your OpenAI API key. If you don't have one, sign up for OpenAI and generate your API key.

## Running the Streamlit App

1. Clone the repository or download the code files.

    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2. Open the `app.py` file in your preferred code editor.

3. Replace `"menation your api key"` with your actual OpenAI API key.

4. Save the changes.

5. Run the Streamlit app using the following command:

    ```bash
    streamlit run app.py
    ```

6. A new browser window or tab should open, displaying the Streamlit app.

## Using the App

1. In the Streamlit app, you'll see a text area where you can enter your prompt for the email. The default prompt is set to "Dear [Name],\n\n".

2. Customize the prompt by editing the text in the input area.

3. Click the "Generate Email" button to trigger the GPT-3.5-turbo model to generate a response based on your prompt.

4. The generated email will be displayed below the button.

5. Experiment with different prompts and generate emails for various scenarios.

6. Close the Streamlit app when you're done.

Feel free to explore and modify the code to suit your specific use case.

---

This guide provides a step-by-step explanation for setting up and using the Email Generation app. Users can follow these instructions to run the app locally and generate emails using the OpenAI GPT-3.5-turbo model.
