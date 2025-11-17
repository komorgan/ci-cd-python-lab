# ci-cd-python-lab

![CI](https://img.shields.io/github/actions/workflow/status/komorgan/ci-cd-python-lab/ci.yml?branch=main)

A minimal Python package to demonstrate CI/CD with GitHub Actions.

## Local setup

```bash
python3 -m venv .venv        # optional but recommended
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pip install -e .
