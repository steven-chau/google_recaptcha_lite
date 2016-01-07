# Import the Flask Framework
from flask import Flask, render_template, request
from google_recaptcha_lite import GoogleRecaptchaLite

GOOGLE_RECAPTCHA_SECRET = 'YOUR SECRET GOES HERE'

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/process-form', methods=['POST'])
def process_form():
    userName = request.form.get('name')
    userResp = request.form.get('g-recaptcha-response')
    # remoteIp = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

    captchalite = GoogleRecaptchaLite(GOOGLE_RECAPTCHA_SECRET)
    apiJson = captchalite.verify(userResp)
    # apiJson = captchalite.verify(userResp, remoteIp)

    if apiJson['success']:
        return userName + ', you have passed Google Recaptcha!'
    else:
        return userName + ', you have failed Google Recaptcha! Error: ' +  ' '.join( apiJson['error-codes'] )


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
