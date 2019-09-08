#endpoint not related to restapi just helpers endpoints or action endpointis
# you can define other endpoints user related and not related to REST API
from ..app import app

@app.route('/whoami')
def whoami():
    # return user logged
    # pending token validtion!
    return {'myuser':'myuser'}

