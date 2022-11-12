FROM ubuntu:20.04


RUN  export DEBIAN_FRONTEND=noninteractive
ENV  DEBIAN_FRONTEND noninteractive
RUN  dpkg-divert --local --rename --add /sbin/initctl
RUN apt update
RUN apt-get -y install ca-certificates openssh-server supervisor rpl openssh-client
COPY ./src/supervisord.conf /etc/supervisor.conf

#ssh
RUN mkdir /var/run/sshd
COPY ./src/sshd.conf /etc/supervisor/conf.d/sshd.conf
RUN rpl "PermitRootLogin without-password" "PermitRootLogin yes" /etc/ssh/sshd_config
RUN sed -i "s/.*PasswordAuthentication.*/PasswordAuthentication yes/g" /etc/ssh/sshd_config

#depends
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y libc6 g++ libc-dev manpages-dev libc-dev-bin sudo && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
#  apt-get install -y curl htop man wget && \
  rm -rf /var/lib/apt/lists/* 


#journalctl fix
# RUN apt update && apt install -y upstart syslog-ng
RUN mkdir /run/log/journal
COPY ./src/test.journal /run/log/journal/test.journal

#User
RUN useradd test -G sudo -m
RUN echo test:qwerty123 | chpasswd

RUN echo 'root:R3Ally_H4RD_PASSWORD_C4NT_GU3SS_1T' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

USER root
RUN echo "test ALL=(ALL:ALL) NOPASSWD:/bin/journalctl -n15" > /etc/sudoers
RUN echo "CTF{all_suD0_RRRRRights_maTTer}" > /root/flag.txt

#start
CMD ["supervisord", "-c", "/etc/supervisor.conf"]

