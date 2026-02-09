from flask import Flask, request

app = Flask(__name__)


@app.route(
    "/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "DELETE", "PATCH"]
)
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def catch_all(path):
    print(f"\n--- Incoming Request: {request.method} /{path} ---")
    print(f"Headers: \n{request.headers}")
    print(f"Args: {request.args}")
    print(f"Body: {request.get_data(as_text=True)}")
    return {"status": "success", "echo_path": path}, 200


if __name__ == "__main__":
    app.run(port=5000)
