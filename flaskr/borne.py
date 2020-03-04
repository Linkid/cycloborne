import datetime

from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_babel import _

from flaskr.db import get_db
from flaskr.forms import AskForm


#
# register the bp
#
bp = Blueprint('borne', __name__)


@bp.route('/ask', methods=('GET', 'POST'))
def ask():
    db = get_db()

    # result
    result = dict()
    ## today
    sql = """
    SELECT
        SUM(cycle_dist) AS nb_km,
        COUNT(b.id) AS nb_id
    FROM borne b
    WHERE DATETIME(cycle_datetime) >= DATETIME('now')
    """
    # WHERE DATETIME(cycle_datetime) >= DATETIME('2019-05-14')
    result_today = db.execute(sql).fetchone()
    result['nb_id_today'] = result_today['nb_id']
    result['nb_km_today'] = result_today['nb_km']

    ## total
    sql = """
    SELECT
        SUM(cycle_dist) AS nb_km,
        COUNT(b.id) AS nb_id
    FROM borne b
    """
    result_total = db.execute(sql).fetchone()
    result['nb_id_total'] = result_total['nb_id']
    result['nb_km_total'] = result_total['nb_km']

    # form
    form = AskForm()
    if form.validate_on_submit():
        data = (
            form.cycle_time.data,
            form.cycle_dist.data,
            form.cycle_type.data
        )
        print(data)

        sql = 'INSERT INTO borne (cycle_time, cycle_dist, cycle_type) VALUES (?, ?, ?)'
        db.execute(sql, data)
        db.commit()

        flash(_("Thank you!"))
        return redirect(url_for('borne.ask'))

    return render_template('borne/ask.html', form=form, result=result)


@bp.route('/show')
def show():
    db = get_db()

    sql = 'SELECT b.id, cycle_datetime, cycle_time, cycle_dist, cycle_type FROM borne b'
    print(sql)
    results = db.execute(sql).fetchall()
    #print(results)

    return render_template('borne/show.html', results=results)


@bp.route('/admin')
def admin():
    return render_template('borne/admin.html')
