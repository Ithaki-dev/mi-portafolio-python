from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

num_random = random.randint(1, 100)
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
current_year = datetime.datetime.now().year
def get_gender(user_name):
        # Use the Genderize API
    response = requests.get(f'https://api.genderize.io?name={user_name}')
    gender = response.json().get('gender')
    return gender

def get_age(user_name):
    # Use the Agify API
    response = requests.get(f'https://api.agify.io?name={user_name}')
    age = response.json().get('age')
    return age

# @app.route('/<string:user_name>')
# def home(user_name):
#     user_age = get_age(user_name)
#     user_gender = get_gender(user_name)

#     return render_template('index.html', name=user_name, age=user_age, gender=user_gender)

@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/3083c920e6d9c3d71c94'
    response = requests.get(blog_url)
    blog_posts = response.json()
    return render_template('blog.html', posts=blog_posts)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
