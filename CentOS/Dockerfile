FROM centos/systemd as binary-base

USER root

# setup yum correctly 
# WORKDIR /etc/yum.repos.d/
# RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
#RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

# install make, cmake, gcc, g++, python3 and python3 libraries
RUN yum update -y
RUN yum install git -y
RUN yum install -y cmake make
RUN yum update cmake make
RUN yum groupinstall -y "Development Tools"
RUN yum install -y python3-devel 


# RUN yum install -y python-pip
RUN python3 -m pip install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install ez_setup
RUN pip3 install matplotlib
RUN pip3 install numpy scipy 
# setup repo
WORKDIR /daq
RUN git clone -b master https://github.com/eudaq/eudaq.git

# create build folder and run cmake
RUN mkdir -p /daq/eudaq/build
WORKDIR /daq/eudaq/build
RUN yum upgrade cmake 
RUN cmake -D EUDAQ_BUILD_PYTHON=ON ..

# install software with make
RUN make install

# activate SSH Server for debug reasons
RUN yum install -y epel-release
RUN yum install -y openssh-server openssh-clients
RUN systemctl start sshd
EXPOSE 22
# CMD ["/usr/sbin/sshd","-D"]