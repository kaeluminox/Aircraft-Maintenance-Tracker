readme_content = '''# Aircraft Maintenance Tracker ✈️

A web-based application for recording and tracking aircraft maintenance tasks, built with Python and Flask. Developed as a capstone project connecting software development skills with an Airframe Powerplant background.

## Features

- **Add maintenance records** — log aircraft/component, task, status, and date
- **View all records** — see every maintenance entry in a clean table
- **Edit records** — update existing entries as task status changes
- **Delete records** — remove entries that are no longer needed
- **Filter by status** — quickly view tasks by Pending, In Progress, or Completed
- **Dashboard** — visual summary with a pie chart and stat cards showing task counts by status

## Tech Stack

- **Python 3** — backend logic
- **Flask** — web framework (routing, templates)
- **SQLite3** — local database for storing maintenance records
- **HTML / Jinja templates** — page rendering with dynamic data
- **CSS** — custom styling for a clean, consistent interface
- **Chart.js** — data visualization for the dashboard

## What I Learned

This project was my introduction to full-stack web development:

- Structuring a Flask application: routes, templates, and request handling (GET vs POST)
- Connecting a Python backend to an SQLite database with full CRUD operations
- Using Jinja templating to render dynamic data inside HTML
- Building a simple data visualization with Chart.js, fed by data from the backend
- Writing and organizing custom CSS across multiple pages
- Debugging real-world issues — mismatched folder names, browser caching, and CSS selectors affecting unintended elements

## How to Run

1. Make sure Python 3 is installed
2. Clone this repository
3. Install Flask:
pip install flask
4. Run the app:
python "Aircraft Maintenance Tracker.py"
5. Open your browser to:http://127.0.0.1:5000/

## Screenshots

**Home**
![Home Page](screenshots/home.png)

**Add Data**
![Add Maintenance Data](screenshots/add_data.png)

**View Data**
![View Maintenance Data](screenshots/view_data.png)

**Dashboard**
![Dashboard](screenshots/dashboard.png)

## About This Project

I built this project as a capstone assignment connecting my Airframe Powerplant background to software development. Rather than a generic CRUD app, this tool reflects a real use case from the aviation maintenance world — tracking the status of maintenance tasks across aircraft and components.
'''

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("README.md berhasil ditulis ulang!")