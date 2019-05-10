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
    form = AskForm()

    if form.validate_on_submit():
        db = get_db()
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

    return render_template('borne/ask.html', form=form)


@bp.route('/show')
def show():
    db = get_db()

    sql = 'SELECT b.id, cycle_datetime, cycle_time, cycle_dist, cycle_type FROM borne b'
    print(sql)
    results = db.execute(sql).fetchall()
    #print(results)

    return render_template('borne/show.html', results=results)


@bp.route('/ask1', methods=('GET', 'POST'))
def ask1():
    if request.method == 'POST':
        cycle_datetime = datetime.date.today()
        cycle_time = request.form['cycle_time']
        cycle_dist = request.form['cycle_dist']
        cycle_type = request.form['cycle_type']
        db = get_db()
        error = None

        if not cycle_time:
            error = _('Time is required')
        elif not cycle_dist:
            error = _('Distance is required')
        elif not cycle_type:
            error = _('Type is required')

        if error is None:
            sql = 'INSERT INTO borne (cycle_datetime, cycle_time, cycle_dist, cycle_type)'
            db.execute(sql, (cycle_datetime, cycle_time, cycle_dist, cycle_type))
            db.commit()
            flash(_("Thank you!"))
            #return redirect(url_for('borne.thanks'))
            return redirect(url_for('borne.ask'))

        flash(error)

    return render_template('borne/ask1.html')
