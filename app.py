from flask import Flask, render_template, request, session
import os
import random

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'classroom-development-only-key')

ATTACKS = ['Punch', 'Kick', 'Fireball']


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'health' not in session:
        session['health'] = 100

    message = 'Choose your attack!'

    if request.method == 'POST':
        choice = request.form.get('attack', '')

        if choice == 'Restart':
            session['health'] = 100
            message = 'A new monster appeared!'
        elif choice in ATTACKS and session['health'] > 0:
            damage = random.randint(0, 100)
            session['health'] = max(0, session['health'] - damage)
            message = f'You used {choice}! -{damage} HP'
        else:
            message = 'Choose a valid attack.'

    return render_template('index.html', health=session['health'], attacks=ATTACKS, message=message)


if __name__ == '__main__':
    app.run(debug=True)
