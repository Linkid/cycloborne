import datetime

from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_babel import _
from sqlalchemy import func
from sqlalchemy.sql.functions import coalesce

from flaskr import db
from flaskr.forms import AskForm
from flaskr.models import Borne


#
# register the bp
#
bp = Blueprint('borne', __name__)


@bp.route('/ask', methods=('GET', 'POST'))
def ask():

    # result
    result = dict()

    ## total result
    #SELECT
    #    SUM(cycle_dist) AS nb_km,
    #    COUNT(b.id) AS nb_id
    #FROM borne b
    result_total = db.session.query(
        func.count(Borne.id).label('nb_id'),
        coalesce(func.sum(Borne.cycle_dist), 0).label('nb_km'),
    )
    result_total_ = result_total.first()
    result['nb_id_total'] = result_total_.nb_id
    result['nb_km_total'] = result_total_.nb_km

    ## today result
    #WHERE DATETIME(cycle_datetime) >= DATETIME('now')
    result_today = result_total.filter(
        func.datetime(Borne.cycle_datetime) >= datetime.datetime.now()
    )
    result_today_ = result_today.first()
    result['nb_id_today'] = result_today_.nb_id
    result['nb_km_today'] = result_today_.nb_km

    # form
    form = AskForm()
    if form.validate_on_submit():
        # insert data
        data = Borne(
            cycle_time=form.cycle_time.data,
            cycle_dist=form.cycle_dist.data,
            cycle_type=form.cycle_type.data
        )
        db.session.add(data)
        db.session.commit()
        print(data)

        flash(_("Thank you!"))
        return redirect(url_for('borne.ask'))

    return render_template('borne/ask.html', form=form, result=result)


@bp.route('/show')
def show():
    # get the selected element and remove it
    print(request.args.get('id'))

    # get all elements to display them
    results = Borne.query.all()

    return render_template('borne/show.html', results=results)


@bp.route('/admin')
def admin():
    return render_template('borne/admin.html')
