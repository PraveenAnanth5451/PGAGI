# TalentScout AI Hiring Assistant

## Project Overview
TalentScout AI Hiring Assistant is an intelligent chatbot designed to streamline the initial screening process for technology candidates. The chatbot automates the collection of candidate information and generates relevant technical questions based on the candidate's declared tech stack. It provides a seamless, interactive experience for both candidates and recruiters.

### Key Features
- Interactive chat interface using Streamlit
- Automated collection of candidate information
- Dynamic technical question generation
- Context-aware conversation flow
- Support for multiple technology stacks
- Real-time response generation

## Installation Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

### Setup Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd talent-scout-ai
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Access the application at http://localhost:8501

## Usage Guide

### For Candidates
1. Open the application in your web browser
2. The chatbot will greet you and ask for your name
3. Follow the prompts to provide your information:
   - Full Name
   - Email Address
   - Phone Number
   - Years of Experience
   - Desired Position
   - Current Location
4. List your technical skills when prompted (comma-separated)
5. Answer the generated technical questions
6. Type 'exit' or 'bye' to end the conversation

### For Recruiters
1. Access the application through the provided URL
2. Monitor candidate responses in real-time
3. Review collected information and technical answers
4. Make informed decisions based on candidate responses

## Technical Details

### Libraries and Frameworks
- **Streamlit**: Frontend framework for creating interactive web applications
- **Python**: Core programming language
- **Requests**: HTTP library for API calls (if needed)

### Architecture
- **Frontend**: Streamlit-based chat interface
- **Backend**: Python-based logic and state management
- **State Management**: Streamlit Session State
- **Data Storage**: In-memory (Session-based)

### Key Components
1. **Chat Interface**
   - Real-time message display
   - User input handling
   - Response generation

2. **Information Collection**
   - Structured data gathering
   - Input validation
   - State management

3. **Question Generation**
   - Technology-specific questions
   - Dynamic response generation
   - Fallback mechanisms

## Prompt Design

### Information Gathering Prompts
The chatbot uses carefully crafted prompts to:
1. Maintain a professional tone
2. Guide candidates through the process
3. Collect information systematically
4. Handle edge cases gracefully

### Technical Question Generation
Questions are generated based on:
1. Candidate's declared tech stack
2. Industry best practices
3. Common interview patterns
4. Technology-specific challenges

### Conversation Flow
The chatbot maintains context through:
1. Stage-based progression
2. Clear transition messages
3. Consistent formatting
4. Error handling

## Challenges & Solutions

### 1. API Integration Challenges
**Challenge**: Initial attempts to use external APIs (Gemini, DeepSeek) faced authentication and availability issues.

**Solution**: 
- Implemented a local rule-based system
- Created a predefined question database
- Added fallback mechanisms for unknown technologies

### 2. State Management
**Challenge**: Maintaining conversation context and user information across sessions.

**Solution**:
- Utilized Streamlit's session state
- Implemented structured data storage
- Created clear state transition logic

### 3. Question Generation
**Challenge**: Generating relevant and challenging technical questions.

**Solution**:
- Created a comprehensive question database
- Implemented technology-specific question sets
- Added fallback generic questions

### 4. User Experience
**Challenge**: Ensuring smooth and intuitive interaction.

**Solution**:
- Implemented clear prompts and instructions
- Added error handling and recovery
- Created a responsive chat interface

## Future Enhancements

### Planned Features
1. Database Integration
   - Persistent storage
   - Candidate history
   - Analytics dashboard

2. Advanced Features
   - Natural Language Processing
   - Sentiment Analysis
   - Custom Question Sets

3. Integration Capabilities
   - ATS Systems
   - Calendar Integration
   - Email Notifications

## Contributing
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
For support, please open an issue in the repository or contact the development team. 