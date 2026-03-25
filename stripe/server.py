import os
import stripe
from flask import Flask, redirect, request

app = Flask(__name__, static_folder='public', static_url_path='')

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

YOUR_DOMAIN = os.environ.get('SERVER_ADDRESS', 'http://localhost:4242').rstrip('/')


@app.route('/checkout.html')
def checkout():
    return app.send_static_file('checkout.html')


@app.route('/success.html')
def success():
    return app.send_static_file('success.html')


@app.route('/cancel.html')
def cancel():
    return app.send_static_file('cancel.html')


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    session = stripe.checkout.Session.create(
        line_items=[{
            'price': 'price_1TA6HH5wgVagseSWdh6YUpo3',
            'quantity': 1,
        }],
        mode='subscription',
        success_url=YOUR_DOMAIN + '/success.html',
        cancel_url=YOUR_DOMAIN + '/cancel.html',
    )
    return redirect(session.url, code=303)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4242, debug=True)
