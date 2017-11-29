"""Landing Blueprint."""
from flask import Blueprint, render_template

landing_handler = Blueprint(name='landing',
                            import_name=__name__,
                            template_folder='templates',
                            static_folder='static')


@landing_handler.route('/', methods=['GET'])
def landing():
    """Render landing page."""
    return render_template('landing.html')
