from flask import Flask, url_for, session
from flask import render_template, redirect
from authlib.integrations.flask_client import OAuth
import google
import webhook_discord
import datetime

# Discord Config
web_hook_url = "https://discordapp.com/api/webhooks/708841556571848725/zJoGnm5jKbS6y6WRf5xCUKB4fIo7v0L2VBzemRa6pGkoeBYwzLgd9IhQ75cUeqGkLC6q"
# Date Time Config
_CURR_DATE = datetime.datetime.today()
_CURR_DAY_START = _CURR_DATE.replace(hour=0, minute=0, second=0, microsecond=0)
_CURR_DAY_END = _CURR_DAY_START + datetime.timedelta(1)
_CURR_DAY_START_NS = int(_CURR_DAY_START.timestamp()) * 1000000000
_CURR_DAY_END_NS = int(_CURR_DAY_END.timestamp()) * 1000000000

# Data Source ID Config
#sourceid = "derived:com.google.calories.expended:com.google.android.gms:merge_calories_expended"
#sourceid ='derived:com.google.calories.expended:com.google.android.gms:from_activities'
sourceid = 'derived:com.google.calories.expended:com.google.android.gms:platform_calories_expended'

# Flask Config Stuff
app = Flask(__name__)
app.secret_key = '!secret'
app.config.from_object('config')

# Google Oath + Scope
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth = OAuth(app)
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile https://www.googleapis.com/auth/fitness.activity.read'
        # Scope as defined in google developer consol
    }
)

# Flask Routes
@app.route('/')
def homepage():
    # Start Flask user 'Session'
    user = session.get('user')
    return render_template('home.html', user=user)


@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route('/auth')
def auth():
    # Get Token and User data
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)

    # Start Flask user 'Session'
    session['user'] = user

    # Request google for json of calories
    g_response = google.request(access_token=token["access_token"], dataSourceId=sourceid, start=_CURR_DAY_START_NS,
                                end=_CURR_DAY_END_NS)
    print(user['name'])
    # Send to Discord
    data = {"content": f"{user['name']} has burnt {str(int(g_response))} calories today!"}
    webhook_discord.send(data=data, webhook_url=web_hook_url)

    # return to homepage / root directory
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

