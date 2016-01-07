import urllib2, urllib, json

# Module information:
# https://github.com/steven-chau/google_recaptcha_lite

# See documentation
# https://developers.google.com/recaptcha/docs/verify
VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"

class GoogleRecaptchaLite(object):
    def __init__(self, secret):
        self.secret = secret

    def verify(self, userResponse, remoteIp=None):
        request = urllib2.Request (
            url = VERIFY_URL,
            data = urllib.urlencode({
                "secret": self.secret,
                "response": userResponse,
                "remoteip": remoteIp
            }),
            headers = {
                "Content-type": "application/x-www-form-urlencoded",
                "User-agent": "GoogleRecaptchaLite - Python Module"
            }
        )

        apiResponseFp = urllib2.urlopen(request)
        jsonObj = json.load(apiResponseFp)
        return jsonObj
