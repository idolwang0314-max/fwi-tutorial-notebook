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
└── notebooks/
    └── 01-fwi-quickstart.ipynb    # The tutorial
```

## References

- `deepwave` — [github.com/ar4/deepwave](https://github.com/ar4/deepwave) by Alan Richardson
- Virieux, J., & Operto, S. (2009). *An overview of full-waveform inversion in exploration geophysics.* Geophysics, 74(6).
- Tarantola, A. (1984). *Inversion of seismic reflection data in the acoustic approximation.* Geophysics, 49(8).

## License

MIT. See [`LICENSE`](LICENSE).
