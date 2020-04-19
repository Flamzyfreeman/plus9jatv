from app import app

# app.config['FLASK_APP'] = app
# app.config['FLASK_DEBUG'] = True
# app.config['FLASK_ENV'] = 'development'
# app.config['FLASK_RUN_PORT'] = 8080

if __name__ == "__main__":
    app.run(debug=True)
