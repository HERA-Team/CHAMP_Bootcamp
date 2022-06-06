unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=MacOS;;
    *)          machine="UNKNOWN:${unameOut}"
esac

echo "Hello, you are using a ${machine} machine."

url="https://repo.anaconda.com/miniconda/Miniconda3-latest-${machine}-x86_64.sh"

echo "Downloading ${url}"
curl -o miniconda.sh ${url}
sh miniconda.sh
rm -f miniconda.sh

curl -o env.yml https://raw.githubusercontent.com/HERA-Team/CHAMP_Bootcamp/main/Precamp/hera_env.yml
conda env create -f env.yml
rm -f env.yml

curl -o env.yml https://raw.githubusercontent.com/HERA-Team/CHAMP_Bootcamp/main/Precamp/21cmfast_env.yml
conda env create -f env.yml
rm -f env.yml
