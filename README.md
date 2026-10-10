# 👹 Monster Battle — Flask Classroom Game

A beginner-friendly web version of Monster Battle. Practice Python variables, lists, loops, conditions, `random.randint()`, HTML, and Flask routes.

## Get started

1. Clone the repository (replace the URL with your GitHub repository):

   ```bash
   git clone https://github.com/YOUR-USERNAME/monster-battle.git
   cd monster-battle
   ```

2. Create and activate a virtual environment (recommended):

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows PowerShell**
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install Flask:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the game:

   ```bash
   python app.py
   ```

5. Open **http://127.0.0.1:5000** in your browser.

## How to play

- The monster starts with 100 HP.
- Choose Punch, Kick, or Fireball.
- Each attack deals random damage from 0 to 100.
- Defeat the monster and click Restart to play again.

## Student challenges

1. Change the monster emoji and attack names.
2. Give each attack a different damage range.
3. Add player health and monster counterattacks.
4. Add a second monster after winning.

## Project files

- `app.py`: Python game logic and Flask route.
- `templates/index.html`: HTML page, buttons, and Jinja loops.
- `requirements.txt`: Python dependencies.

**Teacher note:** Flask's `session` remembers health across clicks. The default secret key is only for local classroom development. For deployment, set a strong private `SECRET_KEY` environment variable and turn off debug mode.
