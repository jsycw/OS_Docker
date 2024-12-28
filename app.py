from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask & Docker App</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background: radial-gradient(circle, #1e3c72, #2a5298);
                color: #f7f7f7;
                text-align: center;
            }
            .container {
                max-width: 600px;
                padding: 20px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
            }
            h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
                color: #ffd700;
            }
            p {
                font-size: 1.2em;
                margin: 10px 0 20px;
                color: #f0e68c;
            }
            a {
                display: inline-block;
                padding: 10px 20px;
                font-size: 1em;
                color: #1e3c72;
                background: #f7f7f7;
                border-radius: 5px;
                text-decoration: none;
                transition: all 0.3s ease-in-out;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            a:hover {
                background: #ffd700;
                color: #1e3c72;
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Flask & Docker</h1>
            <p>Run your web apps effortlessly inside a Docker container.</p>
            <a href="https://docker.com" target="_blank">Learn More About Docker</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')