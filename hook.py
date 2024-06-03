from flask import Flask, request

app = Flask(__name__)

@app.route('/notifications', methods=['POST'])
def notifications():
    # Extract the JSON content of the request
    data = request.headers

    # Here you can process the data
    print(data)

    # Return a 200 status code to acknowledge receipt of the notification
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, ssl_context=('fullchain.pem', 'privkey.pem'))
