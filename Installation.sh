#!/bin/bash

echo "----- Installation Starts -----\n"

echo "----- Installation Python -----\n"

apt-get install -y python3-pip
apt-get install -y python-pip
apt-get install -y dnspython

echo "----- Installation pip -----\n"

apt install pip

echo "----- Installation go -----\n"

apt install -y gccgo-go
apt install -y golang-go

echo "----- Installation tools -----\n"

apt-get install theharvester

apt install -y libpcap-dev #Need for Install Naabu

apt install naabu


