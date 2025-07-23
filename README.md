=====================================DAY 1=========================
NOTE : Install all the dependecies in virtual Enviroment(eg conda/python)
for conda : conda create -p venv(name of the vertual env) python==3.12(greater than 3.10) -y

✅ Project Structure Completed
Designed and organized the folder structure for scalability and modularity.

Separated core components (agents, data, utils, etc.) for clean code maintenance.

🤖 Code Executor Agent
Built an Agent that can safely execute code snippets dynamically.

Supports Python (other languages support coming soon).

Ensures execution isolation and returns real-time output or error.

📊 Data Analyzer Module
Developed a Data Analyzer that:

Accepts CSV/Excel data files.

Performs basic EDA (Exploratory Data Analysis).

Outputs summaries, visualizations, and insights.

👥 Team Agent Setup
Created a multi-agent architecture simulating a team:

CodeExecutorAgent: For dynamic code execution.

DataAnalyzerAgent: For data interpretation.

ProjectManagerAgent: For task planning (coming soon).

Enables collaborative analysis through agent interaction.


🚀 Features
✅ Chat Input Interface
Interact with an AI chatbot via a clean and responsive chat UI.

✅ File Upload
Upload .pdf, .txt, or .docx files to be analyzed and used in the chat context (e.g., summarization, Q&A, extraction).

✅ Message Saving
All user and assistant messages are saved in a database or local storage to allow chat history retrieval and seamless continuity.

✅ Load Saved States
Previously saved chats are loaded when a user returns, ensuring continuity in conversation even after refreshing the browser or relaunching the app.

✅ Project Completion
All core modules—chat input, file handling, storage integration, and state management—have been successfully implemented, making the project feature-complete.