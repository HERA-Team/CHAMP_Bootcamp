unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=MacOS;;
    *)          machine="UNKNOWN:${unameOut}"
esac

echo "Hello, you are using a ${machine} machine."

curl https://repo.anaconda.com/miniconda/Miniconda3-latest-${machine}-x86_64.sh | sh

curl -o hera_env.yml https://github.com/HERA-Team/CHAMP_Bootcamp/blob/main/Precamp/hera_env.yml
conda env create -f env.yml
rm -f env.yml

curl -o env.yml https://github.com/HERA-Team/CHAMP_Bootcamp/blob/main/Precamp/21cmfast_env.yml
conda env create -f env.yml
rm -f env.yml
