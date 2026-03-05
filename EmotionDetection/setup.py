from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='minhtth5',
    description='A package to detect emotions using Watson NLP',
)
