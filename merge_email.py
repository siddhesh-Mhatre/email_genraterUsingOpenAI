import streamlit as st
import openai
import smtplib

# Set up your OpenAI API key
openai.api_key = "KEY"

# Function to generate email using GPT-3
def generate_email(prompt, email_type):
    model_engine = "gpt-3.5-turbo-instruct"

    if email_type == "Formal":
        prompt += "\nSincerely,\n[Your Name]"
    elif email_type == "Informal":
        prompt += "\nBest regards,\n[Your Name]"
    elif email_type == "Business":
        prompt += "\nKind regards,\n[Your Name]"

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
    )

    return response.choices[0].text

# Function to send email
def send_email():
    recipient_email = st.text_input("Recipient Email:")
    subject = st.text_input("Subject:")
    message = st.text_area("Message:")

    if st.button("Send Email"):
        email = "thakurtcsceduanjali@gmail.com"
        smtp_password = "Your pass"
        smtp_server = "smtp.gmail.com"

        text = f"Subject:{subject}\n\n{message}"
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()
        server.login(email, smtp_password)
        server.sendmail(email, recipient_email, text)
        server.quit()

        st.success(f"Email has been sent to {recipient_email}")

# Streamlit app with two tabs
def main():
    st.title("Email App")

    # Tab selection
    tab = st.sidebar.selectbox("Select Tab:", ["Generate Email", "Send Email"])

    if tab == "Generate Email":
        st.subheader("Generate Email")
        input_text = st.text_area("Enter your prompt for the email:", "Dear [Name],\n\n")
        email_type = st.selectbox("Select the type of email:", ["Formal", "Informal", "Business"])

        if st.button("Generate Email"):
            response = generate_email(input_text, email_type)
            st.subheader("Generated Email:")
            st.write(response)
    elif tab == "Send Email":
        st.subheader("Send Email")
        send_email()

if __name__ == "__main__":
    main()
