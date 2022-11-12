FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install xinetd dos2unix -y

RUN useradd -m easyheap

ADD --chown=root:root ./share/run.sh /home/easyheap/
ADD --chown=root:root ./share/flag.txt /home/easyheap/
ADD --chown=root:root ./share/easyheap /home/easyheap/easyheap
ADD --chown=root:root xinetd /etc/xinetd.d/easyheap

RUN chmod +x /home/easyheap/run.sh
RUN chmod +x /home/easyheap/easyheap

RUN chmod 774 /tmp
RUN chmod -R 774 /var/tmp
RUN chmod -R 774 /dev
RUN chmod -R 774 /run
RUN chmod 1733 /tmp /var/tmp /dev/shm

RUN chown -R root:root /home/easyheap/
RUN dos2unix /etc/xinetd.d/easyheap

EXPOSE 40012/tcp

CMD ["/usr/sbin/xinetd","-dontfork"]
