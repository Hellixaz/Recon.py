#!/bin/bash

printf "----- Installation Starts -----\n"

printf "----- Installation Python -----\n"

apt-get install -y python3-pip
apt-get install -y python-pip
apt-get install -y dnspython

printf "----- Installation pip -----\n"

apt install pip

printf "----- Installation go -----\n"

apt install -y gccgo-go
apt install -y golang-go

printf "----- Installation tools -----\n"

apt-get install theharvester

apt install -y libpcap-dev #Need for Install Naabu

apt install naabu


