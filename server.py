from flask_app import app
from flask_app.controllers import andycontroller

from waitress import serve

#if __name__=="__main__":
#    app.run(debug=True)

serve(app, host='0.0.0.0', port=8080, threads=1)

