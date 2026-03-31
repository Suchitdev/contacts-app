from flask import Flask, render_template, request, redirect
import boto3
import uuid

app = Flask(__name__)


dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('contacts')

@app.route('/')
def home():
    response = table.scan()
    contacts = response.get('Items', [])
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']

    table.put_item(
        Item={
            'contact_id': str(uuid.uuid4()),
            'name': name,
            'phone': phone,
            'email': email
        }
    )
    return redirect('/')

@app.route('/delete/<id>')
def delete_contact(id):
    table.delete_item(Key={'contact_id': id})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)