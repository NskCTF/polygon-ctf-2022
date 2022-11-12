# Название: Lucky Number
## Описание:
SEVEN-SEVEN-SEVEN=jackpot?
### Флаг: 
CTF{w3b_asm_enjoy3r_BD0nspuH7}
### Хинт:
Assembly in web?
### Решение:
Видим, что запросы к серверу не идут, в консоли разработчика можно нажать "Sources"/"Источники" и выкачать сайт, захостить на локалке для дальнейшего анализа
Патчим wasm и js проверки на число 777
##### 1 - патчим JS
`wasm2wat release.wasm > release.txt`
ну тут без комментариев, убираем `if (random === 777) document.body.innerText = "Really out of luck"; и делаем чтобы random всегда был равен 777`
##### 2 - патчим WASM
Ctrl-F <= 777, число встретится 2 раза
```
Строка "NOPE"
(data (;19;) (i32.const 2024) "\01\00\00\00\08\00\00\00N\00O\00P\00E") <= i32.const 2032

if (a == 777) {
g_k = g_k + 20;
return 2032;
} (то же в псевдокоде) команда: wasm-decompile release.wasm > a.txt
```
пробуем заменить первое (чтобы число 777 обрабатывалось как остальные)
(заменяем 777 к примеру на 555)
`wat2wasm release.txt` - конвертируем обратно, закидываем в папку с сайтом и получаем флаг:  
`You roll this number: 777; result:CTF{w3b_asm_enjoy3r_BD0nspuH7}`