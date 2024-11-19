# wart-dapp


## Build on MacOS (Arm64)
```shell
brew install python@3.10

python3.10 -m venv wart-py310

source wart-py310/bin/activate

python -m pip install -r requirements.txt

rm -rf build dist

python -m PyInstaller main-arm64.spec

./dist/wart-dapp/wart-dapp

# you could use this node (from https://github.com/warthog-network/public-nodes/blob/master/nodes.txt)
http://62.72.44.89:3001 # blu & Asia

deactivate


```