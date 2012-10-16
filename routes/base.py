from flask import render_template

class Base():
    def render(self, template, **data):
        return render_template(template + '.html', **data)
    
    def not_found(self):
        return self.render('errors/404')