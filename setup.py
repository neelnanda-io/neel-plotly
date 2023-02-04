from setuptools import setup

setup(
    packages=["neel_plotly"],
    description="Neel's personal Plotly utils - you're welcome to use, but this is very badly maintained and commented!.",
    install_requires=[
        "einops",
        "numpy",
        "torch",
        "plotly",
        "tqdm",
        "pandas",
    ],
)
