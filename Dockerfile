FROM ubuntu:20.04

ARG hostname
ARG host_ip
ARG ros_master_uri
RUN apt update

ENV TZ=Asia/Vladivostok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros-latest.list'
RUN apt install -y curl gnupg gnupg2 gnupg1
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -
RUN apt update && apt install -y ros-noetic-ros-base
ENV ROS_DISTRO=noetic
RUN apt install -y python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
#Сервер SSH
RUN apt install -y openssh-server
RUN apt install -y wiringpi
#PID-Контроллер управлением скоростью вращения колес
RUN apt install -y ros-noetic-pid 
#Установка пакетов Bluetooth для джостика
RUN apt install -y software-properties-common
RUN apt install -y bluetooth bluez bluez-tools
RUN apt install -y python3-venv python3-pip
RUN apt install -y python-is-python3 
RUN pip3 install ds4drv
#Библиотека для использования GPIO-контактов Paspberry PI
RUN git clone https://github.com/WiringPi/WiringPi.git
#Драйвер геймпада DualShock 4
RUN apt -y install python3-venv python3-pip
RUN apt -y install python-is-python3
RUN pip3 install ds4drv
RUN git clone https://github.com/naoki-mizuno/ds4_driver.git
#ROS-пакет для управлением джостиком
RUN apt -y install ros-noetic-joy
# Драйвер лидара RPLIDAR A1
RUN git clone https://github.com/Slamtec/rplidar_ros.git
#Построение карты
RUN apt install -y ros-noetic-gmapping

ENV PROJECT_DIR=/root/ros
ENV ROS_MASTER_URI=${ros_master_uri}
WORKDIR /root/ros
COPY .bashrc /root/
