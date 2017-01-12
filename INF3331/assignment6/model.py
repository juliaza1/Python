from wtforms import Form, validators, IntegerField, SelectField, FloatField, StringField


class InputF(Form):
    Start = IntegerField(label='[from 1751]', default=1751, validators=[validators.InputRequired()])
    End = IntegerField(label='[til 2012]', default=2012, validators=[validators.InputRequired()])


class InputForm(Form):
    Month = SelectField(label=" ", choices=[('January', 'January'), ('February', 'February'), ('March', 'March'),
                                            ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'),
                                            ('August', 'August'), ('September', 'September'), ('October', 'October'),
                                            ('November', 'November'), ('December', 'December')],
                        validators=[validators.InputRequired()])
    Start = IntegerField(label='[from 1816]', default=1816, validators=[validators.InputRequired()])
    End = IntegerField(label='[til 2012]', default=2012, validators=[validators.InputRequired()])
    Ymin = IntegerField(label=' ', default=-5, validators=[validators.InputRequired()])
    Ymax = IntegerField(label=' ', default=5, validators=[validators.InputRequired()])


class InputCity(Form):
    Year = StringField(label='[from 1960 to 2013]', default=2013, validators=[validators.InputRequired()])
    T1 = FloatField(label='Upper threshold', default=15, validators=[validators.InputRequired()])
    T2 = FloatField(label='Lower threshold', default=1, validators=[validators.InputRequired()])
