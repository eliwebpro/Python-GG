from flask import Flask, render_template, request

app = Flask(__name__)

# Convertemos a lista de tuplas em um dicionário para o inventário
inventory_data = [
    ("Curb-mount Flashing", 0),
    ("Deck Mount", 0),
    ("Deck-mount Flashing", 0),
    ("ECL 1446", 14),
    ("ECL 2246", 16),
    ("ECL 2270", 1),
    ("ECL 3046", 4),
    ("ECL 3055", 0),
    ("ECL 3446", 1),
    ("ECL 4646", 4),
    ("ECL 4672", 0),
    ("EDL 106", 6),
    ("EDL 112", 4),
    ("EDL 156", 7),
    ("EDL 308", 5),
    ("EDL 606", 2),
    ("EDL A06", 2),
    ("EDL C06", 30),
    ("EDL C12", 5),
    ("EDL M08", 14),
    ("EDL S06", 7),
    ("EDM D06", 0),
    ("EDM D26", 1),
    ("EDM M08", 1),
    ("EDM S06", 0),
    ("ECW 2270", 2),
    ("FCM 1430 L", 0),
    ("FCM 1430 T", 2),
    ("FCM 1446 L", 0),
    ("FCM 1446 T", 6),
    ("FCM 2222 L", 5),
    ("FCM 2222 T", 13),
    ("FCM 2222 WL", 5),
    ("FCM 2230 L", 3),
    ("FCM 2230 T", 3),
    ("FCM 2234 L", 3),
    ("FCM 2234 T", 1),
    ("FCM 2246 L", 10),
    ("FCM 2246 L 08D", 3),
    ("FCM 2246 T", 8),
    ("FCM 2270 L", 4),
    ("FCM 2270 T", 0),
    ("FCM 3030 L", 4),
    ("FCM 3030 T", 0),
    ("FCM 3046 L", 1),
    ("FCM 3046 T", 0),
    ("FCM 3055 L", 2),
    ("FCM 3434 L", 4),
    ("FCM 3434 T", 0),
    ("FCM 3446 L", 1),
    ("FCM 3446 T", 0),
    ("FCM 4622 L", 0),
    ("FCM 4622 T", 0),
    ("FCM 4646 L", 5),
    ("FCM 4646 T", 1),
    ("FS A06 (00W)", 1),
    ("FS C01", 3),
    ("FS C04", 5),
    ("FS C06", 7),
    ("FS C06PA00", 1),
    ("FS C08", 3),
    ("FS C08CS00", 0),
    ("FS C12", 0),
    ("FS D06", 2),
    ("FS D26", 4),
    ("FS M02", 2),
    ("FS M04", 2),
    ("FS M06", 2),
    ("FS M08", 0),
    ("FS M08CS00", 1),
    ("FS S01", 1),
    ("FS S06", 2),
    ("FSR M02", 1),
    ("FX 2222", 10),
    ("FX 2246", 15),
    ("FX 3030", 6),
    ("FX 3434", 5),
    ("FX 4646", 5),
    ("FXG 225225 (2222)", 0),
    ("FXG 225465 (2246)", 0),
    ("FXG 345345 (3434)", 0),
    ("FXG 465465 (4646)", 0),
    ("Self-Flashed", 0),
    ("TCC 014", 3),
    ("TCR 014", 2),
    ("TGF 022", 3),
    ("TGR 010", 7),
    ("TGR 014", 11),
    ("THR 010", 2),
    ("THR 014", 1),
    ("TIL, CK06, C06, 8888", 3),
    ("TMF 014", 1),
    ("TMR 010", 10),
    ("TMR 014", 19),
    ("TSH, C06, C01, 1016S", 1),
    ("TSH, C01, 1016SWL", 1),
    ("ZCC, C04, 1045SWL", 3),
    ("ZCD, D06, 1163SWL", 1),
    ("ZCE, M06, 306, 1045S", 1),
    ("ZCE, P04, 404, 1045S", 2),
    ("ZCE, PK10, 1045S", 2),
    ("ZCCC, 2246, 1045SWL", 4),
    ("ZCCC, 2246, 1158 S", 2),
    ("ZCCC, 2234, 1155S", 2),
    ("ZCCC, 4646, 1045SWL", 1),
    ("ZSCC, 2246, 1045SWL", 6),
    ("ZSCC, 4622, 1155S", 1),
    ("ZSCD, C04, 1045SWL", 3),
    ("ZSCD, D06, 1163SWL", 1)
]

# Convertemos a lista de tuplas em um dicionário para o inventário
inventory = {item[0]: item[1] for item in inventory_data}

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
