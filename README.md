## boc-curve
Par yields are what's quoted, but discount factors are what you actually need to value anything, and the transformation is non-trivial, so I built it rather than importing it.

![Zero curve](output/zero_curve.png)

Bootstraps a zero curve from Government of Canada benchmark yields and decomposes daily curve moves into level, slope, and curvature factors.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Methodology

TODO

## Assumptions and limitations

TODO