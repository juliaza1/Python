from flask import Flask, render_template, request

from model import InputForm, InputF, InputCity
from temperature_CO2_plotter import plot_temperature, plot_co2, plot_co2_by_country

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def root():
    return render_template('select.html')


@app.route('/view/', methods=['GET', 'POST'])
def temp():
    form = InputForm(request.form)

    if request.method == 'POST' and form.validate():
        result = plot_temperature(form.Month.data, form.Start.data, form.End.data, form.Ymin.data, form.Ymax.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)


@app.route('/view2/', methods=['GET', 'POST'])
def co2():

    form = InputF(request.form)
    if request.method == 'POST' and form.validate():
        result_2 = plot_co2(form.Start.data, form.End.data)

    else:
        result_2 = None

    return render_template('view2.html', form=form, result_2=result_2)


@app.route('/view3/', methods=['GET', 'POST'])
def co2_cities():

    form = InputCity(request.form)
    if request.method == 'POST' and form.validate():
        result_3 = plot_co2_by_country(form.Year.data, form.T1.data, form.T2.data)

    else:
        result_3 = None

    return render_template('view3.html', form=form, result_3=result_3)

if __name__ == '__main__':
    app.run(debug=True)
