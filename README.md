# google_recaptcha_lite
This is a Python library to help you verify a user's response to Google's reCAPTCHA.

## Demonstration
http://goog-recaptcha-lite.appspot.com/


## Credits
This Python module was derived from this project:
https://github.com/sirjhep/gRecaptcha4py


## Usage
1. Copy the file `google_recaptcha_lite.py` to your project.
2. In your Python script that handles the verification of reCAPTCHA, do this:
  1. Import this module: `from google_recaptcha_lite import GoogleRecaptchaLite`
  2. Include something like this: 
  ```
    userResp = request.form.get('g-recaptcha-response')
    captchalite = GoogleRecaptchaLite(GOOGLE_RECAPTCHA_SECRET)
    apiJson = captchalite.verify(userResp)

    if apiJson['success']:
        return 'You have passed Google Recaptcha!'
    else:
        return 'You have failed Google Recaptcha!'
  ```

See `example_on_gae` for a full example of using this module on Google App Engine.
