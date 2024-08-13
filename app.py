from flask import Flask, render_template, request, url_for, redirect, flash
import pandas as pd

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    search_query = ""
    items = []

    if request.method == 'POST':
        search_query = request.form.get('search_query', '')

    # Load data from CSV
    df = pd.read_csv('data.csv')
    items = df.to_dict(orient='records')

    if search_query:
        items = [item for item in items if search_query.lower() in item['title'].lower()]

    return render_template('index.html', items=items, search_query=search_query)

if __name__ == '__main__':
    app.run(debug=True)
