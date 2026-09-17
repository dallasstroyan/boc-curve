## boc-curve
Bootstraps a zero curve from Government of Canada benchmark yields and decomposes daily curve moves into level, slope, and curvature factors.

Par yields are what's quoted, but discount factors are what you actually need to value anything, and the transformation is non-trivial. This implements that transformation directly rather than importing a library that handles it.

**Status:** in development. The import layer is working; Data clean-up and organization is next, with bootstrapping to follow. See the road map below

## Roadmap
- [x] **Data Import** - Bank of Canada Valet API client with response validation and timestamped raw snapshots
- [ ] **Data Handling** - Cache and organize the data in a robust structure 
- [ ] **Bootstrap** - par yields to discount factors to zero rates, validated by repricing the input bonds off the fitted curve
- [ ] **Forwards** - 1y1y, 2y1y, and 5y5y implied forwards tracked against the BoC overnight rate to show what the curve is pricing in
- [ ] **PCA** - level, slope, and curvature factors extracted from daily curve changes, with variance explaned and factor time series
- [ ] **Reporting** - one command regenerats the full chart pack from cache
- [ ] **Validation** - cross-check the bootstrapped curve against QuantLib

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.fetch
```

## Structure
- src/    analysis code
- data/   cached raw and processed data (gitignored)
- output/ generated charts (gitignored)
- assets/ charts published
- tests/  unit tests

## Methodology

*Data sources.* Government of Canada benchmark bond yields and treasury bill yields from the Bank of Canada Valet API.

*Conventions.* Semi-annual compounding, ACT/365 - the Government of Canada market convention. Set once in 'src/config.py' and applied consistiently downstream

*Interpolation.* (TODO)

## Assumptions and limitations

- **Benchmark yields are not true par yields.** The Bank publishes yields on specific on-the-run bonds with off-round maturities and non-par coupons. Treating these as par yields is an approximation; the error is small at current coupon levels but not zero.
- **The long benchmark has a drifting maturity.** 'BD.CDN.LONG.DQ.YLD' tracks whicheven bond is currently the long benchmark, so its actual maturity moves and jumps at each new issue. It is mapped to a nominal 30 years here.
- **Sparse coverage past 10 years.** The benchmark set has no point betwen 10 and 30 years, so the long end leans heavily on the interpolation scheme.
- **No liquidity or financing adjustment.** On-the-run bonds trade rich to the curve; that spread is not modelled. 