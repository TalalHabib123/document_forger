from setuptools import setup, find_packages

setup(
    name='document_forger',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'pytesseract',
        'pillow',
        'pandas',
        'tqdm',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'document_forger=src.__main__:main',
        ],
    },
    include_package_data=True,
    description='A package for generating forged documents',
    author='',
    author_email='',
    url='', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)

