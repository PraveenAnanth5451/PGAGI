import streamlit as st
import json

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []
    # Add initial greeting message
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello! I'm the TalentScout AI Hiring Assistant. I'll help you through our initial screening process. Could you please tell me your full name?"
    })

# Initialize session state for candidate info
if 'candidate_info' not in st.session_state:
    st.session_state.candidate_info = {
        'name': '',
        'email': '',
        'phone': '',
        'experience': '',
        'position': '',
        'location': '',
        'tech_stack': []
    }

# Initialize session state for conversation stage
if 'stage' not in st.session_state:
    st.session_state.stage = 'info_gathering'

def generate_technical_questions(tech_stack):
    """Generate technical questions based on the tech stack"""
    questions = []
    tech_list = [tech.strip().lower() for tech in tech_stack]
    
    # Define questions for different technologies
    tech_questions = {
        'python': [
            "1. Explain the difference between lists and tuples in Python.",
            "2. How do you handle exceptions in Python?",
            "3. What are decorators in Python and how do you use them?"
        ],
        'javascript': [
            "1. Explain the concept of closures in JavaScript.",
            "2. What is the difference between let, const, and var?",
            "3. How do you handle asynchronous operations in JavaScript?"
        ],
        'java': [
            "1. Explain the difference between HashMap and HashTable.",
            "2. What is the difference between abstract class and interface?",
            "3. How does garbage collection work in Java?"
        ],
        'react': [
            "1. Explain the concept of virtual DOM in React.",
            "2. What are hooks in React and how do you use them?",
            "3. How do you handle state management in React applications?"
        ],
        'node.js': [
            "1. Explain the event loop in Node.js.",
            "2. How do you handle errors in Node.js applications?",
            "3. What is the difference between process.nextTick() and setImmediate()?"
        ],
        'sql': [
            "1. Explain the difference between INNER JOIN and LEFT JOIN.",
            "2. What are indexes and when would you use them?",
            "3. How do you optimize a slow-running query?"
        ],
        'aws': [
            "1. Explain the difference between EC2 and Lambda.",
            "2. What is the purpose of IAM roles?",
            "3. How do you handle high availability in AWS?"
        ]
    }
    
    # Generate questions based on the tech stack
    for tech in tech_list:
        for key, value in tech_questions.items():
            if key in tech:
                questions.extend(value[:2])  # Take first 2 questions for each matching technology
    
    # If no specific questions were generated, provide generic questions
    if not questions:
        questions = [
            "1. Describe a challenging technical problem you've solved recently.",
            "2. How do you stay updated with the latest technologies in your field?",
            "3. Explain your approach to debugging complex issues."
        ]
    
    return "\n".join(questions[:5])  # Return up to 5 questions

def process_user_input(user_input):
    """Process user input based on conversation stage"""
    if 'exit' in user_input.lower() or 'bye' in user_input.lower():
        return "Thank you for your time! We'll review your information and get back to you soon. Have a great day!"

    if st.session_state.stage == 'info_gathering':
        # Update candidate info based on the current field being collected
        if not st.session_state.candidate_info['name']:
            st.session_state.candidate_info['name'] = user_input
            return "Thank you! Could you please provide your email address?"
        elif not st.session_state.candidate_info['email']:
            st.session_state.candidate_info['email'] = user_input
            return "Great! What's your phone number?"
        elif not st.session_state.candidate_info['phone']:
            st.session_state.candidate_info['phone'] = user_input
            return "How many years of experience do you have?"
        elif not st.session_state.candidate_info['experience']:
            st.session_state.candidate_info['experience'] = user_input
            return "What position are you interested in?"
        elif not st.session_state.candidate_info['position']:
            st.session_state.candidate_info['position'] = user_input
            return "What's your current location?"
        elif not st.session_state.candidate_info['location']:
            st.session_state.candidate_info['location'] = user_input
            st.session_state.stage = 'tech_stack'
            return "Please list your technical skills, including programming languages, frameworks, databases, and tools you're proficient in. You can separate them with commas."
    
    elif st.session_state.stage == 'tech_stack':
        st.session_state.candidate_info['tech_stack'] = [tech.strip() for tech in user_input.split(',')]
        st.session_state.stage = 'technical_questions'
        return generate_technical_questions(st.session_state.candidate_info['tech_stack'])
    
    elif st.session_state.stage == 'technical_questions':
        return "Thank you for your answers! We'll review your profile and get back to you soon. Type 'exit' to end the conversation."

# Streamlit UI
st.title("TalentScout AI Hiring Assistant")
st.write("Welcome to TalentScout's AI-powered hiring assistant. I'll help you through our initial screening process.")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate and display assistant response
    response = process_user_input(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response) 