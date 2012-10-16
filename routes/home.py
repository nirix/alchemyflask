from base import Base
from db import session
from models import Example

class Home(Base):
    def index(self):
        examples = session.query(Example).all()
        return self.render('examples/index', examples=examples)
