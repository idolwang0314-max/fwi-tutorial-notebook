# fwi-tutorial-notebook

A self-contained Jupyter notebook walking through **Full Waveform Inversion (FWI)**
on a synthetic 2D velocity model, using [`deepwave`](https://github.com/ar4/deepwave)
for differentiable wave-equation simulation in PyTorch.

> Audience: anyone who has heard "FWI" and wants to see it work end-to-end in
> ~100 lines of Python. Runs on CPU in a couple of minutes; faster on a GPU.

## What you'll learn

In one notebook you will:

1. Build a synthetic 2D velocity model with a buried high-velocity anomaly
2. Set up a multi-shot surface acquisition (sources + receivers + Ricker wavelet)
3. Generate "observed" seismic data via the scalar acoustic wave equation
4. Define a poor initial guess (uniform velocity)
5. Recover the true model by minimizing an L2 data misfit through Adam, with
   gradients computed end-to-end through the wave solver
6. Compare the inverted model against the truth

No prior FWI knowledge required — concepts are introduced as they show up.

## Ultrasound FWI literature library / 超声 FWI 文献库

[Browse the literature library](literature/ultrasound-fwi/README.md): **151 records**
with contributions, methods, validation evidence, limitations, and public sources.
The Chinese research review combines earlier literature work with searches through
**September 26, 2026**, focusing on Ultrasonics, IEEE TUFFC/TUSON, Geophysics/GJI,
Imperial College, and Yubing Li.

- [研究综述](literature/ultrasound-fwi/REVIEW_CN.md) · [26 篇精读排序](literature/ultrasound-fwi/READING_RANKING.md)
- [总索引](literature/ultrasound-fwi/INDEX.md) · [分类](literature/ultrasound-fwi/CLASSIFICATION.md) · [作者路线](literature/ultrasound-fwi/AUTHOR_MAP.md)
- [CSV](literature/ultrasound-fwi/library.csv) · [BibTeX](literature/ultrasound-fwi/references.bib) · [JSON](literature/ultrasound-fwi/library.json)

The library also includes a standalone HTML search interface for offline use and
standard-library Python scripts for rebuilding the catalog. See its
[README](literature/ultrasound-fwi/README.md) for instructions and evidence levels.

## Setup

```bash
# Recommended: create a fresh environment
conda create -n fwi-tutorial python=3.10 -y
conda activate fwi-tutorial

pip install -r requirements.txt
jupyter lab notebooks/01-fwi-quickstart.ipynb
```

If you have a CUDA GPU, the notebook will use it automatically. Otherwise it
runs on CPU (slower but fine for this demo size).

## What you should see

The notebook produces three velocity-model panels at the end — left to right:
**true** | **initial (uniform)** | **FWI result**. The FWI result should clearly
recover the layer interface and the buried anomaly, even though the initial
guess was a constant 1700 m/s.

## Files

```
fwi-tutorial-notebook/
├── README.md                      # You are here
├── LICENSE                        # MIT
├── requirements.txt
├── notebooks/
│   └── 01-fwi-quickstart.ipynb     # The tutorial
└── literature/
    └── ultrasound-fwi/            # Curated literature, indexes and exports
```

## References

- `deepwave` — [github.com/ar4/deepwave](https://github.com/ar4/deepwave) by Alan Richardson
- Virieux, J., & Operto, S. (2009). *An overview of full-waveform inversion in exploration geophysics.* Geophysics, 74(6).
- Tarantola, A. (1984). *Inversion of seismic reflection data in the acoustic approximation.* Geophysics, 49(8).

## License

MIT. See [`LICENSE`](LICENSE).
