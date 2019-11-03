from nameko.standalone.rpc import ClusterRpcProxy


CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost"}

@app.route('/hello', methods=['POST'])
def hello():
    with ClusterRpcProxy(CONFIG) as rpc:
        result = rpc.greeting_service.hello(name="jerry")
        return result, 200

app.run(debug=True)