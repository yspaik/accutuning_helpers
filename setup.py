from setuptools import setup, find_namespace_packages
setup(
    name="accutuning_helpers",
    version="1.0.30",
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=[
        "numpy==1.19.5",
        "pandas==1.1.4",
        "scikit-learn==0.23.2",
        "scipy==1.5.2",
        "joblib==1.1.0",
        "python-dateutil==2.8.2",
        "ctgan==0.4.3",
        "sentence-transformers==0.3.9",
    ]
)
