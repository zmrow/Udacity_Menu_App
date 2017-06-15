from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/restaurants')
def show_restaurants():
    pass


@app.route('/restaurant/new')
def new_restaurant():
    pass


@app.route('/restaurant/<int:restaurant_id>/edit')
def edit_restaurant():
    pass


@app.route('/restaurant/<int:restaurant_id>/delete')
def delete_restaurant():
    pass


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def show_menu():
    pass

@app.route('/restaurant/<int:restaurant_id>/menu/new')
def new_menu_item():
    pass


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def edit_menu_item():
    pass


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def delete_menu_item():
    pass


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
