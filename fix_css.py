css_content = '''body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #F4F8FB;
    color: #1B4F72;
    margin: 0;
    padding: 0;
}

nav {
    background-color: #4A90D9;
    padding: 15px 20px;
}

nav a {
    color: white;
    text-decoration: none;
    margin-right: 20px;
    font-weight: bold;
}

nav a:hover {
    text-decoration: underline;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 30px;
}

table {
    border-collapse: collapse;
    width: 100%;
    background-color: white;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

th, td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: #4A90D9;
    color: white;
}

form input, form select {
    padding: 8px;
    margin-bottom: 15px;
    width: 250px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #4A90D9;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #1B4F72;
}

a.delete-btn {
    color: #E07A5F;
}

.stat-card {
    background-color: white;
    padding: 20px 30px;
    margin-bottom: 15px;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    text-align: center;
}

.stat-number {
    font-size: 36px;
    font-weight: bold;
    color: #4A90D9;
}

.stat-label {
    color: #1B4F72;
    font-size: 14px;
}

.form-card {
    background-color: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    max-width: 400px;
}
'''

with open("static/style.css", "w") as f:
    f.write(css_content)

print("style.css berhasil ditulis ulang!")