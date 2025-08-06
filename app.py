from flask import Flask, send_from_directory #importing Flask from flask module
from routes import api_routes #having routes in a separate file

app = Flask(__name__, static_folder='static', static_url_path='') #telling Flask where to look for resources

@app.route('/')
def serve_index():
  return send_from_directory('static', 'index.html')

#registering the blueprint
app.register_blueprint(api_routes)#telling Flask to include the routes from the routes.py file

if __name__=="__main__": #entry point
  app.run(host="0.0.0.0", port=8000, debug=True)#starting flask in debug mode