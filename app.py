from flask import Flask #importing Flask from flask module
from routes import api_routes #having routes in a separate file
send__from__directory
@app.route('/')
def serve_index()
  return send__from__directory('static', 'index.html')
app= Flask(__name__) #telling Flask where to look for resources
#registering the blueprint
app.register_blueprint(api_routes)#telling Flask to include the routes from the routes.py file
if __name__=="__main__": #entry point
  app.run(debug=True)#starting flask in debug mode
