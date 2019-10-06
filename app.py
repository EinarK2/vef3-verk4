from flask import Flask, render_template
import csv
from PIL import Image

with open('frett.csv', 'r', newline='', encoding='utf-8') as file:
	reader = list(csv.reader(file, delimiter=':'))

for x in range(len(reader)):
	reader[x].append(reader[x][0].replace(' ', '-'))

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('selection.tpl', len=len(reader), list=reader)

@app.route("/frett/<int:frett>")
def frett(frett):
	efni = reader[int(frett)]

	with Image.open("static/Mynd"+str(frett)+".jpg") as img:
		width, height = img.size

	return render_template('article.tpl', index=frett, titill=efni[0], grein=efni[1], netfang=efni[2], height=height*(485/width))

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)

@app.errorhandler(404)
def error(error):
	return render_template('error.tpl')
