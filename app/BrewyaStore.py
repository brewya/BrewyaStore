import flask
import magic

app = flask.Flask(__name__)

static_data = {}

def replace_vars(data):
    data = data.replace("{this_server_url}", flask.request.url_root.rstrip("/"))
    return data

@app.route("/")
def hello():
    return '', 204

@app.route("/api/v1/status")
def status():
    return '', 204

@app.route("/api/v1/console_configuration")
def console_configuration():
    return '''{
    "BTC_LAUNCHER_PACKAGES": "tv.ouya.xbmc,tunein.player,tv.twitch.android.viewer,com.plexapp.android,tv.ouya.bbciplayer,tv.ouya.hulu,tv.ouya.minecrafttv,tv.ouya.ouyabrowser,tv.ouya.pandora,tv.ouya.visiomgo,tv.ouya.youtube,tv.ouya.tubitv"
}'''

@app.route("/api/v1/ratings")
def ratings():
    return '''{
    "ratings": []
}'''

@app.route("/api/v1/details")
def details():
    tmp = None
    with open("app/data/games/{}/detail.json".format(flask.request.args.get('app'))) as f:
        tmp = "\n".join(f.readlines())
    return tmp

@app.route("/api/v1/apps/<uuid>/download")
def apps_download(uuid):
    tmp = None
    with open("app/data/games/{}/download.json".format(uuid)) as f:
        tmp = "\n".join(f.readlines())
    return tmp

@app.route("/api/v1/apps/<uuid>/<resource>")
def apps_resource(uuid, resource):
    filename = "app/data/games/{}/static/{}".format(uuid, resource)
    mime = magic.from_file(filename, mime=True)
    with open(filename,'rb') as f:
        return flask.Response(b"".join(f.readlines()), mimetype=mime)

@app.route("/api/v1/sessions", methods=['POST'])
def sessions():
    return '''{
    "token": "7e9d69a1-311d-4add-b410-faf969ed499c"
}'''

@app.route("/api/v1/gamers/me/consoles", methods=['GET', 'POST', 'PUT'])
def gamers_consoles():
    return '{}'

@app.route("/api/v1/gamers/key", methods=['PUT', 'POST'])
def gamers_key():
    return '{}', 201

@app.route("/api/v1/premium_purchases", methods=['GET'])
def premium_purchases():
    return '{ "games": [] }'

@app.route("/api/v1/gamers/me", methods=['GET'])
def gamers_me():
    return '''{
  "gamer": {
    "uuid": "f791f35c-697c-4d4b-8298-783e70622ef2",
    "settings": {},
    "founder": false,
    "email": "nobody@brewya.tv",
    "username": "BrewyaUser"
  }
}'''

@app.route("/api/v1/wallet")
def wallet():
    return '''{
    "balance": 0.0, 
    "credit_card": null, 
    "currency": "USD", 
    "requiresPaymentMethod": false
}'''

@app.route("/api/v1/gamers/me/agreements")
def gamers_me_agreements():
    return '''{
    "marketplace": 2, 
    "marketplace_required_version": 2, 
    "privacy": 0, 
    "privacy_required_version": 0
}'''

@app.route("/api/v1/discover/home")
def discover_home():
    return '''{
    "heroRow": null, 
    "rows": [
    {
        "ranked": false, 
        "showPrice": true, 
        "tiles": [], 
        "title": "Featured"
    }
    ], 
    "tiles": [], 
    "title": "home"
}'''

@app.route("/api/v1/discover")
def discover():
    return replace_vars(static_data['discover'])


if __name__ == "__main__":
    with open("app/data/discover.json","r") as f:
        static_data['discover'] = "\n".join(f.readlines())
    app.run(host='0.0.0.0')
