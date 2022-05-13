from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from game_app.models import Collection, VideoGame
from game_app.main.forms import CollectionForm, VideoGameForm
from game_app.extensions import db, app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home')
def home():
    all_collections = Collection.query.all()
    return render_template('home.html', all_collections=all_collections)


@main.route('/new_collection', methods=['GET', 'POST'])
@login_required
def new_collection():
    form = CollectionForm()

    if form.validate_on_submit():
        new_collection = Collection(
            name = form.name.data,
            description = form.description.data,
            created_by = current_user
        )

        db.session.add(new_collection)
        db.session.commit()

        flash(f"Collection: '{new_collection.name}' was succesfully created")
        return redirect(url_for('main.collection_details', collection_id=new_collection.id))
    return render_template('new_collection.html', form=form)


@main.route('/collection/<collection_id>', methods=['GET', 'POST'])
@login_required
def collection_details(collection_id):
    collection = Collection.query.get(collection_id)
    original_name = collection.name
    original_description = collection.description
    form = CollectionForm(obj=collection)

    if form.validate_on_submit():
        collection.name = form.name.data
        collection.description = form.description.data

        db.session.add(collection)
        db.session.commit()

        if collection.name != original_name and original_description == collection.description:
            flash(f"'{original_name}' has been updated to '{collection.name}'")
        else:
            flash('Collection has been updated')

        return redirect(url_for('main.collection_details', collection_id=collection.id))
    return render_template('collection_details.html', form=form, collection=collection)


@main.route('/new_game', methods=['GET', 'POST'])
@login_required
def new_game():
    form = VideoGameForm()

    if form.validate_on_submit():
        new_game = VideoGame(
            title = form.title.data,
            rating = form.rating.data,
            description = form.description.data,
            collection = form.collection.data,
            created_by = current_user
        )

        db.session.add(new_game)
        db.session.commit()

        flash(f"Collection: '{new_game.title}' was added to {new_game.collection}")
        return redirect(url_for('main.game_details', game_id=new_game.id))
    return render_template('new_game.html', form=form)


@main.route('/videogame/<game_id>', methods=['GET', 'POST'])
@login_required
def game_details(game_id):
    game = VideoGame.query.get(game_id)
    form = VideoGameForm(obj=game)

    if form.validate_on_submit():
        game.title = form.title.data
        game.rating = form.rating.data
        game.description = form.description.data
        game.collection = form.collection.data

        db.session.add(game)
        db.session.commit()

        flash(f'{game.title} has been updated')
        return redirect(url_for('main.game_details', game_id=game.id))

    return render_template('game_details.html', form=form, game=game)