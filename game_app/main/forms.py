from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms_sqlalchemy.orm  import QuerySelectField
from wtforms.validators import DataRequired, Length
from game_app.models import Collection

class CollectionForm(FlaskForm):
    '''Collection Form (adding/updating)'''
    name = StringField('Collection Name', validators=[DataRequired(), Length(min=2, max=80)])
    description = StringField('Collection Description', validators=[DataRequired(), Length(min=1, max=400)])
    submit = SubmitField('Add Collection')

class VideoGameForm(FlaskForm):
    '''Video Game Form (adding/updating)'''
    title = StringField('Game Title', validators=[DataRequired(), Length(min=2, max=80)])
    rating = FloatField('Game Rating (out of 5.0)', validators=[DataRequired()])
    description = StringField('Game Description', validators=[DataRequired(), Length(min=1, max=400)])
    collection = QuerySelectField('Collection', query_factory=lambda: Collection.query, get_label='name')
    submit = SubmitField('Add Game')
    
