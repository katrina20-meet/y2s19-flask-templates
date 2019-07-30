from flask import Flask, render_template
app = Flask(__name__)
opposite_day= True

@app.route('/')
def home_page():
    food = ["pizza", "curry", "moghrayeh"] 
    return render_template(
"index.html",
food=food,
no_food=False)

if __name__ == '__main__':
   app.run(debug = True)
