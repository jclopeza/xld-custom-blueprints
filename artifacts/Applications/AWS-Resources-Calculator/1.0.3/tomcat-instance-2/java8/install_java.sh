echo "add-apt-repository"
sudo add-apt-repository -y ppa:openjdk-r/ppa
echo "update"
sudo apt-get update
echo "install openjdk 8"
sudo apt-get -y install openjdk-8-jre
#sudo update-alternatives --config java
