from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms import RadioField
from wtforms import SubmitField
from wtforms import IntegerField
#from wtforms_components import TimeField
from wtforms.validators import DataRequired
from wtforms.validators import NumberRange


class AskForm(FlaskForm):
    cycle_type_choices = [
        ('classic', _l('Classic')),
        ('vae', _l('VAE')),
    ]
    #cycle_time = TimeField(_l('Time (HH:MM AM)'))
    cycle_time = IntegerField(_l('<strong>Time (min)</strong>'), validators=[NumberRange(min=0, max=200)])
    cycle_dist = FloatField(_l('<strong>Distance (km)</strong>'), validators=[NumberRange(min=0, max=100)])
    cycle_type = RadioField(_l('<strong>Type of bicycle</strong>'), choices=cycle_type_choices, default='classic', validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))
