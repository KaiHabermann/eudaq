FROM dokken/ubuntu-20.04 as binary-base

USER root

# install make, cmake, gcc, g++, python3 and python3 libraries
RUN apt-get update
RUN apt-get install git -y
RUN apt-get install -y cmake make
# RUN apt-get groupinstall -y "Development Tools"
RUN apt-get install -y python3-dev


RUN apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install ez_setup
RUN pip3 install matplotlib
RUN pip3 install numpy scipy 
RUN apt-get install -y python3-tk

# setup repo
WORKDIR /daq
RUN git clone -b master https://github.com/eudaq/eudaq.git

# create build folder and run cmake
RUN mkdir -p /daq/eudaq/build
WORKDIR /daq/eudaq/build
RUN cmake -D EUDAQ_BUILD_PYTHON=ON ..

# install software with make
RUN make install

# activate SSH Server for debug reasons

ARG SSH_MASTER_USER
ARG SSH_MASTER_PASS
RUN apt-get install -y openssh-server 

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    nano \
    sudo \
    openssh-server \
    xauth
COPY ssh_config /etc/ssh/ssh_config
COPY sshd_config /etc/ssh/sshd_config
 
COPY user.sh /usr/local/bin/user.sh
RUN chmod +x /usr/local/bin/user.sh
RUN /usr/local/bin/user.sh
 
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
EXPOSE 22
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
# ENTRYPOINT service ssh restart && bash
# CMD ["/usr/sbin/sshd","-D"]

CMD tail -f /dev/null