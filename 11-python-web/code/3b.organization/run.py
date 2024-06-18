import dotenv, os
dotenv.load_dotenv()  # load FLASK_RUN_PORT

from flask_example import app
app.run(debug=True, port=os.environ["FLASK_RUN_PORT"])
