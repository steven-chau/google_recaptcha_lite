# Demonstrating how to use google_recaptcha_lite

## Prerequisite
You need to have App Engine SDK for Python installed on your machine. See https://cloud.google.com/appengine/docs/python/ for details.

You also need to register a Google reCAPTCHA account to run this example: https://www.google.com/recaptcha


## To run this example locally
1. cd `example_on_gae`
2. Define your `GOOGLE_RECAPTCHA_SECRET` in `main.py`.
3. Define your `sitekey` in `templates/index.html`.
4. `pip install -r requirements.txt -t lib/`
5. `dev_appserver .`


## To deploy to Google App Engine
1. Define your application ID in `app.yaml`.
2. `appcfg.py  --noauth_local_webserver  --oauth2 update .`
