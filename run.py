from app import create_app, db
from app.blueprints.Users.models import User

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'app': create_app, 'db': db, 'User': User,}