class TripIt(object):
    # webauth_credentials and oauth_credentials are for backward compatibility
    # of keyword arguments. Consider them deprecated and instead use either
    # the first positional argument, or the "credential" keyword argument
    # for either type of credential.
    #
    # NOTE that if you were using positional arguments before for anything but
    # webauth credentials, the signature of this constructor has changed, and
    # you will need to update your code to match.
    #
    # Also, note that despite having a default value, the "credential" parameter
    # is NOT optional. In a future release, the default value, and the
    # webauth_credentials and oauth_credentials keyword parameters will be removed.
    def __init__(self, credential = None, api_url='https://api.tripit.com',
                 webauth_credentials = None, oauth_credentials = None):
        self._api_url     = api_url
        self._api_version = 'v1'
        self._credential  = credential or oauth_credentials or webauth_credentials
        self.resource  = None
        self.response  = None
        self.http_code = None
