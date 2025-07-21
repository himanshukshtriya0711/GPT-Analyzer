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