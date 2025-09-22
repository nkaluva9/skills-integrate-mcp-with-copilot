# Integrate MCP with Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey nkaluva9!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

Remember, it's self-paced so feel free to take a break! ☕️

[![](https://img.shields.io/badge/Go%20to%20Exercise-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/nkaluva9/skills-integrate-mcp-with-copilot/issues/1)

---

## Run the application

Correct command (recommended):

```bash
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

Common typo that causes an error:

- `ModuleNotFoundError: No module named 'scr'` — this happens if you run `uvicorn scr.app:app` (missing the "c" in `src`).

For convenience the repository provides a tiny compatibility shim so `uvicorn scr.app:app` also works, but prefer the correct `src.app:app` command.

```bash
# Create and activate a venv (recommended)
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
# Run
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

