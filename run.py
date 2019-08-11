from api import create_api
from api.ws import socketio

if __name__ == '__main__':
  api = create_api()
  socketio.run(api, host="0.0.0.0", port=5000)