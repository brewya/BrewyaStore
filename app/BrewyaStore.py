from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

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

@app.route("/api/v1/sessions", methods=['POST'])
def sessions():
    return '''{
    "token": "7e9d69a1-311d-4add-b410-faf969ed499c"
}'''

@app.route("/api/v1/gamers/me/consoles", methods=['GET', 'POST'])
def consoles():
    return '{}'

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
    return '''{
        "heroRow": null, 
        "rows": [
            {
                "ranked": true, 
                "showPrice": true, 
                "tiles": [], 
                "title": "OUR NEW STORE"
            }, 
            {
                "ranked": false, 
                "showPrice": true, 
                "tiles": [], 
                "title": "JUST A DEMO"
            }, 
            {
                "ranked": false, 
                "showPrice": true, 
                "tiles": [], 
                "title": "NOTHING HERE"
            } 
        ], 
        "tiles": [
        ], 
        "title": "DISCOVER"
    }'''


if __name__ == "__main__":
    app.run(host='0.0.0.0')
