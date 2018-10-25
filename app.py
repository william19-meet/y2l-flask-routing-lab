from flask import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_page.html')
@app.route('/shop')
def shop_page():
	shows = ["The Flash 10$.", "Rick and Morty 20$", "Lcs (jk) free"]
	return render_template('shop.html', shows=shows)


if __name__ == '__main__':
   app.run(debug = True)