# pcdet
from open-mmlab

#create anaconda venv
conda env create -f environment.yml

conda activate pcdet

cd src && cd OpenPCDet

# install dependencies and check
pip install -r requirements

#should take a long time
python setup.py develop

#test
python
import pcdet
