from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return render_template(
        "index.html",
        tasks=tasks
    )

@app.route("/add", methods=["GET", "POST"])
def add_task():

    if request.method == "POST":

        task_name = request.form["task"]

        tasks.append({
            "id": len(tasks) + 1,
            "task": task_name
        })

        return redirect("/")

    return render_template("add_task.html")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):

    global tasks

    tasks = [
        task
        for task in tasks
        if task["id"] != task_id
    ]

    return redirect("/")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
