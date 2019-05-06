from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms import RadioField
from wtforms import SubmitField
from wtforms import IntegerField
#from wtforms_components import TimeField
from wtforms.validators import DataRequired


class AskForm(FlaskForm):
    cycle_type_choices = [
        ('classic', _l('Classic')),
        ('vae', _l('VAE')),
    ]
    #cycle_time = TimeField(_l('Time (HH:MM AM)'))
    cycle_time = IntegerField(_l('Time (HH:MM AM)'), validators=[DataRequired()])
    cycle_dist = FloatField(_l('Distance (km)'), validators=[DataRequired()])
    cycle_type = RadioField(_l('Type of bicycle'), choices=cycle_type_choices, default='classic', validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))
