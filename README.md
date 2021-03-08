# tailwind table lists design
django-tailwind from paiza.cloud

```
git clone https://github.com/sin-sky-sora/tails_tablelist.git
cd firstproject
sh init.sh
source ~/.bash_profile
pyenv install 3.8.8
pyenv global 3.8.8
# pipenv
python -m pip install --upgrade pip
python -m pip install pipenv
pipenv install
```

### start APP 
```
cd ~/tails_tablelist/
pipenv run start

# tailwind css build
pipenv run build
# HTMLに使われてるCSSしかビルドされない!!!

## first build please run
cd tails/static_src/
npm install
cd ../../
pipenv run build
```

### github push
```
git config --global user.email "email@example.com"
git config --global user.name "name"
```
