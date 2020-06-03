TWINE_USERNAME
TWINE_PASSWORD
TWINE_REPOSITORY
TWINE_REPOSITORY_URL

git commit -a -m "commit"
git push -u GitHub master
python3 -m pip install --upgrade pip setuptools wheel twine keyring
python setup.py sdist bdist_wheel 

keyring set https://test.pypi.org/legacy/  j5pu
ó
python3 -m keyring set https://test.pypi.org/legacy/ j5pu

keyring set https://upload.pypi.org/legacy/ j5pu
ó
python3 -m keyring set https://upload.pypi.org/legacy/ j5pu

twine check

twine upload --repository-url https://test.pypi.org/legacy/ dist/*

twine upload dist/*
ó
twine upload dist/* -r pypi
ó
python3 -m twine upload --repository-url https://pypi.org/j5pu/macOS


git tag -a v0.1 -m "first release"
git push GitHub --tags
