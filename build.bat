:: delete files in dist
del /s /q dist

:: build package
python setup.py sdist bdist_wheel

:: upload package
python -m twine upload dist/*