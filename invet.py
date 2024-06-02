from flask import Flask, render_template, request

app = Flask(__name__)

inventory = {
    'item1': 10,
    'item2': 5,
    'item3': 8
}

@app.route('/')
def index():
    return render_template('index.html', inventory=inventory)

@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form['item_name']
    quantity = int(request.form['quantity'])
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    return render_template('index.html', inventory=inventory)

@app.route('/remove', methods=['POST'])
def remove_item():
    item_name = request.form['item_name']
    quantity = int(request.form['quantity'])
    if item_name in inventory and inventory[item_name] >= quantity:
        inventory[item_name] -= quantity
    return render_template('index.html', inventory=inventory)

if __name__ == '__main__':
    app.run(debug=True)
