from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            op = request.form["operation"]

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = "Error (Divide by Zero)" if num2 == 0 else num1 / num2
        except:
            result = "Invalid Input"

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Calculator</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                margin-top: 50px;
                background-color: #f2f2f2;
            }
            input, select {
                padding: 8px;
                margin: 5px;
            }
            button {
                padding: 8px 15px;
                background-color: #4CAF50;
                color: white;
                border: none;
                cursor: pointer;
            }
            h2 {
                color: #333;
            }
        </style>
    </head>
    <body>
        <h2>Simple Flask Calculator</h2>
        <form method="POST">
            <input type="text" name="num1" placeholder="Enter First Number" required>
            <select name="operation">
                <option value="+">+</option>
                <option value="-">-</option>
                <option value="*">*</option>
                <option value="/">/</option>
            </select>
            <input type="text" name="num2" placeholder="Enter Second Number" required>
            <br><br>
            <button type="submit">Calculate</button>
        </form>

        {% if result != "" %}
            <h3>Result: {{ result }}</h3>
        {% endif %}
    </body>
    </html>
    """, result=result)


if __name__ == "__main__":
    app.run(debug=True)
