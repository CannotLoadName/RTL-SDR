from setuptools import setup
setup(
    name="RTL-SDR",
    version="1.0.0",
    author="Enbuging",
    author_email="electricfan@yeah.net",
    license="MIT",
    description="A wrapper for rtlsdr.dll, which can be used to access RTL2832U by software defined radio programs on Microsoft Windows platform.",
    keywords=["radio","SDR","RTL-SDR","RTL2832U","rtlsdr.dll"],
    platforms=["Windows"],
    package_data={
        "rtlsdr":["config.json"]
    },
    install_requires=["numpy>=1.21"],
    packages=["rtlsdr"]
)