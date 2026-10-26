#Full-Stack Expense Tracker

A modern, responsive, full-stack web application for tracking income and expenses, built with Vanilla JavaScript (Frontend) and Python Flask + SQLite (Backend). This project meets all core specifications and acceptance criteria outlined for Task 2 (Expense Tracker) in the CodeNova Full Stack Development Internship Batch 01.🚀 FeaturesDynamic Summary Dashboard: Real-time calculation and display of Total Income, Total Expenses, and Net Balance / Savings Ratio.Dynamic Category Mapping: Automatically updates available transaction categories based on selected type (Income vs Expense) without requiring a page refresh.Dual-Layer Validation:Client-Side Validation: Immediate feedback on form field completion and positive numeric amounts.Server-Side Validation: Python Flask backend independently rejects negative or invalid figures and missing data payload fields.Interactive Data History: Tabular presentation with category badges, sorting, search filtering, and record deletion.Persistent Storage: Uses SQLite database persistence so transaction records survive server restarts.Analytics Visualizations: Visual category breakdowns and income vs. expense trends powered by Chart.js.CSV Data Export: One-click download of all stored financial transaction records as a .csv file.🛠️ Tech Stack & PrerequisitesFrontend: HTML5, CSS3 (Tailwind CSS CDN / Custom CSS), JavaScript (Vanilla ES6)Backend: Python 3.x, Flask, Flask-CORSDatabase: SQLite3Visualization: Chart.js

📂 Repository & Project Directory Structureexpense-tracker/
│
├── env/                  # Python Virtual Environment
├── static/               # Frontend Assets (Styles & Scripts)
│   ├── style.css         # Styling rules
│   └── script.js        # Dynamic UI logic & REST API communications
├── templates/            # HTML Views
│   └── index.html        # Main dashboard interface
├── app.py                # Main Python Flask REST API & SQLite Database logic
├── database.db           # SQLite database file (generated automatically)
├── README.md             # Project handbook and documentation
└── requirements.txt      # Python dependencies

⚙️ Local Setup & Installation GuideFollow these steps to run the project on your local machine:
1. Clone the Repositorygit clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
2. Set Up Virtual EnvironmentCreate and activate the virtual environment:Windows (PowerShell / Command Prompt):python -m venv env
env\Scripts\activate
Windows (Git Bash):source env/Scripts/activate
macOS / Linux:python3 -m venv env
source env/bin/activate
3. Install Required DependenciesEnsure Flask and Flask-CORS are installed:pip install flask flask-cors
4. Run the Application ServerStart the Flask application:python app.py
Open your browser and navigate to:http://127.0.0.1:5000
📡 REST API SpecificationsMethodEndpointDescriptionRequest Body PayloadGET/api/transactionsRetrieves all stored transactionsN/APOST/api/transactionsAdds a new expense or income record{"title": "Salary", "amount": 50000, "type": "income", "category": "salary", "date": "2026-10-26"}DELETE/api/transactions/<id>Deletes record by unique IDN/A📸 Acceptance & Dual-Layer Validation CriteriaPrecision Calculations: Math figures rendered across dashboard cards mirror database aggregations precisely.Server Validation: The Flask API enforces strict validation rules (returns 400 Bad Request if amount <= 0 or if fields are empty) regardless of client interaction.Responsive UI: Fully responsive across mobile, tablet, and desktop viewports.
