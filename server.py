from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

count_get = 0
count_post = 0

@app.route('/')
def route_index():
    return render_template('index.html')

@app.route('/request-counter', methods=['GET', 'POST'])
def route_request_counter():
    global count_post, count_get

    if request.method == 'GET':
        count_get += 1
        return redirect(url_for('route_statistics', count_get=count_get))
    elif request.method == 'POST':
        count_post += 1
        return redirect(url_for('route_statistics', count_post=count_post))
    return render_template('statistics.html')


@app.route('/statistics')
def route_statistics():
    global count_post, count_get

    return render_template("statistics.html", count_post=count_post, count_get=count_get)


if __name__ == "__main__":
    app.run()
