from app import app

@app.route('/')
@app.route('/imdex')
def index():
    return 'Hello!'