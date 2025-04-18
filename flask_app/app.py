from flask import Flask, render_template, request

app = Flask(__name__)

# Route 1: Home with navigation button
@app.route('/')
def home():
    return render_template('home.html')

# Route 2: Form page (GET + POST)
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()

        # Basic error handling
        if not name or not age:
            error = "Please enter both name and age."
            return render_template('form.html', error=error)

        if not age.isdigit() or int(age) <= 0:
            error = "Please enter a valid positive age."
            return render_template('form.html', error=error)

        return render_template('form.html', success=f"Hello {name}, you are {age} years old!")

    return render_template('form.html')
