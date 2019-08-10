import wtforms_json
wtforms_json.init()

from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()