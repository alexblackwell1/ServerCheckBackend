from mcstatus import JavaServer
from flask import Flask

app = Flask(__name__)


@app.route('/api')
def index():
    # server = JavaServer.lookup("ringley.us")
    # status = server.status()
    # return f"The server has {status.players.online} player(s) online and replied in {status.latency} ms"
    print('yes')
    return "no"

if __name__ == '__main__':
    app.run(debug=True)
