from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 冷蔵庫内のアイテムを保存するデータベース（簡単なリストで管理）
inventory = []

@app.route('/')
def index():
    return render_template('index.html', inventory=inventory)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    quantity = request.form['quantity']
    expiration = request.form['expiration']
    
    # アイテムを冷蔵庫に追加
    inventory.append({
        'name': name,
        'quantity': quantity,
        'expiration': expiration
    })
    
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    if 0 <= item_id < len(inventory):
        inventory.pop(item_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
