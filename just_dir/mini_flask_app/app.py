from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_random_cat():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]['url']
    return None

@app.route('/')
def index():
    cat_image = get_random_cat()
    return render_template('index.html', cat_image=cat_image)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
