from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        temp = float(request.form["temperature"])
        conversion = request.form["conversion"]

        if conversion == "CtoF":
            result = (temp * 9/5) + 32
            unit = "°F"

        elif conversion == "FtoC":
            result = (temp - 32) * 5/9
            unit = "°C"

        elif conversion == "CtoK":
            result = temp + 273.15
            unit = "K"

        elif conversion == "KtoC":
            result = temp - 273.15
            unit = "°C"

        result = f"{result:.2f} {unit}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)