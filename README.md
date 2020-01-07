Coloring doesn't work.

It's better to ignore commits (their names aren't good)

---

`separate.py`, `check.py`, `color.py`, `check_color.py` are runnable scripts

classes inside `utils/` are helping classes used in those scripts

---

`raw_data/` should contain original images of plants

`labeled_data/` should contain images of labeled plants  

`separated/`, `masks/` and `boundaries/` have to exist

1. create python interpreter
2. install `opencv-python` (and `numpy` if it's not installed by default)
3. run `separate.py`
4. (optionally) run `check.py` (results will be placed inside `results.txt`)
5. run `color.py`
6. (optionally) run `check_color.py` (results will be placed inside `results_color.txt`)