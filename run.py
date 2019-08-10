from api import create_api

if __name__ == '__main__':
  api = create_api()
  api.run(debug=True, host="0.0.0.0", port="5000")