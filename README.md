# Image Utils

A small Python package to rotate images from Python or the command line.

---

## Installation

### ✅ pip (recommended)

```bash
pip install image-utils-spin
```

---

### ✅ pipx (best for CLI usage)

If you mainly want the CLI command:

```bash
pipx install image-utils-spin
```

---

### ✅ uv

```bash
uv pip install image-utils-spin
```

Or inside a project:

```bash
uv add image-utils-spin
```

---

### ✅ Development (editable install)

For testing or contributing:

```bash
git clone https://github.com/rick-rocks123/image_spinner.git
cd <repo-folder>
pip install -e .
```

---

## Usage

---

### ✅ Command-line usage

After installing, you can use the CLI command `rotate-image` instead of `py main.py`:

```bash
rotate-image input.png 90 output.png
```

Overwrite existing file:

```bash
rotate-image input.png 90 output.png --force
```

---

### ✅ Python usage
## Example 1: direct usage
```python
from image_utils_spin import rotate_image

rotate_image(
    "input.png",
    90,
    "output.png",
    force=True
)
```
## Example 2: usage with CLI-style arguments
```python
from image_utils_spin import rotate_image, argparse_arguments
image_path, rotate_angle, save_path, force = argparse_arguments()

rotate_image(
    image_path,
    rotate_angle,
    save_path,
    force
)
```

### ✅ Bash commands
## Disclaimer: you can use -h or --help
```bash
rotate-image --help
```
or
```bash
py script.py --help
```


