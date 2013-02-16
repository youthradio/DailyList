from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html')


@app.route("/submit", methods=['POST'])
def submission():
	return render_template('response.html')


if __name__ == "__main__":
    app.run(debug=True)
