FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install xinetd dos2unix -y

RUN useradd -m read_me

ADD --chown=root:root ./share/run.sh /home/read_me/
ADD --chown=root:root ./share/flag.txt /home/read_me/
ADD --chown=root:root ./share/read_me /home/read_me/read_me
ADD --chown=root:root xinetd /etc/xinetd.d/read_me

RUN chmod +x /home/read_me/run.sh
RUN chmod +x /home/read_me/read_me

RUN chmod 774 /tmp
RUN chmod -R 774 /var/tmp
RUN chmod -R 774 /dev
RUN chmod -R 774 /run
RUN chmod 1733 /tmp /var/tmp /dev/shm

RUN chown -R root:root /home/read_me/
RUN dos2unix /etc/xinetd.d/read_me

CMD ["/usr/sbin/xinetd","-dontfork"]
