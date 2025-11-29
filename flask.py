from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>I am Home page</h1>
    <h2>I am running in Flask</h2>
    """

@app.route("/about")
def abouta():
    return """
    <h1>I am About page</h1>
    <h2>I am running in Flask</h2>
    """

@app.route("/resume")
def resume():
    return """
    <html>
    <head>
        <title>My Resume</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                margin: 0;
                padding: 20px;
            }
            .container {
                max-width: 900px;
                margin: auto;
                background: white;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            h1, h2 { color: #333; }
            .section {
                margin-bottom: 25px;
            }
            .section h2 {
                border-left: 4px solid #007bff;
                padding-left: 10px;
            }
            .skills span {
                background: #007bff;
                color: white;
                padding: 5px 10px;
                margin: 5px;
                border-radius: 5px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Your Name</h1>
            <p><strong>Web Developer | Programmer | Designer</strong></p>

            <div class="section">
                <h2>Contact</h2>
                <p>Email: youremail@example.com</p>
                <p>Phone: +123 456 7890</p>
                <p>Location: Your City</p>
            </div>

            <div class="section">
                <h2>Summary</h2>
                <p>I am a passionate developer skilled in Python, HTML, CSS, and Flask.</p>
            </div>

            <div class="section">
                <h2>Experience</h2>
                <ul>
                    <li><strong>Job Title — Company (2022–Present)</strong><br>Write your description here.</li>
                    <li><strong>Previous Job — Company (2020–2022)</strong><br>Write your description here.</li>
                </ul>
            </div>

            <div class="section">
                <h2>Education</h2>
                <ul>
                    <li><strong>Bachelor of Computer Science</strong> — Your University</li>
                </ul>
            </div>

            <div class="section skills">
                <h2>Skills</h2>
                <span>Python</span>
                <span>Flask</span>
                <span>HTML</span>
                <span>CSS</span>
                <span>JavaScript</span>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '_main_':
    app.run(debug=True)