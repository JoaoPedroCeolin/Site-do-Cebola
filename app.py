from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ips_visitantes = set()
cliques = 0

@app.route("/")
def home():
    ip = request.remote_addr

    if ip not in ips_visitantes:
        ips_visitantes.add(ip)

    return render_template(
        "index.html",
        visitas=len(ips_visitantes),
        cliques=cliques
    )

@app.route("/click", methods=["POST"])
def click():
    global cliques
    cliques += 1
    return jsonify({"cliques": cliques})

@app.route("/aura")
def aura():
    return render_template("aura.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
