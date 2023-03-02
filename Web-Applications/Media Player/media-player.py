from flask import Flask, render_template, flash, redirect, abort, url_for
import mediaLib


app = Flask(__name__)
app.config["SECRET_KEY"] = "d11cf884bb3bfd05bc65d37660b0b098702c279f2bee06a96804945b814c6dbde6f82371b795f17c7c3fcd2e48fa6410c388109d96b0f886eae0bc78b360adc80b99413df0e0a39dee0e47bedd4032f1cf04ea1c47e4b6199a478e7e58957f820b97f7567a6a356536a0c0a453e00cd5cc56098b25d4873afb4e94bc81ab46490aafa9eb729a7ba8f722bddd73781a6bac85dbaf4d004c193e41ea14012c01f6caab3cc0cb42ed00f827d62f436c1fc938147b8433073275c55e52f002100df6033cd6814d4790a7247a091881fdaa2a79c8ff27f08d592eed2f008045d95eb0c48092854049a8c5e166b60ddc9b018ae81d1006f830c8922d13adf6a552b8eb"




@app.route("/")
def index():
   	return render_template("index.html")

@app.route("/browser")
def browser():
	lib = mediaLib.Library()
	return render_template("browser.html", lib=lib.media)

@app.route("/browser/<movTitle>")
def mediaPlayer(movTitle):
	try:
		media = mediaLib.Library().getMediaByName(movTitle)

		return render_template("media.html", media=media)
	except:
		abort(404)

if __name__ == "__main__":
   	app.run(debug=True, host="0.0.0.0")
   	
