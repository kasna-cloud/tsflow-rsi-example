import setuptools

setuptools.setup(
    name="app",
    version="0.1.0",
    install_requires=[
        "absl-py==0.12.0",
        "apache-beam[gcp]==2.30.0",
        "google-cloud-pubsub==1.7.0",
        "joblib==0.14.1",
        "pandas==1.2.4",
        "plotly==4.14.3",
        "pytest==6.2.4",
        "numpy==1.19.5",
        "scikit-learn==0.24.2",
        "tfx-bsl==0.29.0",
        "tfx==0.29.0",
        "tensorflow==2.4.0",
        "google-auth==1.35.0",
        "fasteners==0.16",
        "pyzmq==21.0.2",
        "pyrsistent==0.17.3",
        "prompt_toolkit==3.0.18",
        "js-regex==1.0.1",
        "jsonschema==3.0.2",
        "parso==0.7.1",
        "pexpect==4.6.0",
        "ptyprocess==0.5.2",
        "nest_asyncio==1.5.0",
        "nbformat==5.0.7",
        "matplotlib_inline==0.1.1",
        "jupyter_core==4.7.0",
        "jedi==0.17.1",
        "jupyter_client==6.0.0",
        "debugpy==1.4.0",
        "markupsafe==2.0.1",
    ],
    packages=setuptools.find_packages(),
)
