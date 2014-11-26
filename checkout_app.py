from flask import Flask, render_template, request
from rentCD import RentCD
app = Flask(__name__)
rent_cd = RentCD()

@app.route('/')
def hello_world():
    customer_id = request.args.get('customer_id')
    cd_id = request.args.get('cd_id')
    rental_contract = rent_cd.checkout(customer_id, cd_id)    
    return render_template ('index.html', rental_contract=rental_contract )

if __name__ == '__main__':
    app.run(debug=True)