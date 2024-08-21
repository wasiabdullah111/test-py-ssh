from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
            }
            .content {
                font-size: 4em; /* 4x larger font */
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="content">
            Hello,  Python app
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

