# Japanese N2 Reader

Static Japanese reading library for GitHub Pages.

## Add a reading

Put a new `.html` file under `readings/`.

Example:

```text
readings/06-new-topic.html
```

The title shown in the sidebar is extracted automatically from the first `<h2>`.

## Generate locally

```bash
python3 generate.py
python3 -m http.server 8000
```

Open `http://localhost:8000`.

## GitHub Pages

Use repository Settings > Pages > Deploy from a branch > `main` > `/ (root)`.

The included GitHub Action regenerates `readings.json` whenever files in `readings/` change.

For that workflow to push the generated JSON, enable:
Settings > Actions > General > Workflow permissions > Read and write permissions.

If your repository does not allow Actions to push, run `python3 generate.py` locally and commit `readings.json`.
