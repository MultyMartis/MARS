# PUBLIC STATUS ACCEPTANCE v1

## Контракт
Для public-пользователя `/my_status` возвращает только его собственный статус:

```text
Ваш статус

Роль: обычный пользователь
Рабочие права: не выданы

Доступно:
<code>/start</code>
<code>/help</code>
<code>/my_status</code>

Чтобы получить права модератора, обратитесь к администратору.
```

Новый public `/start` создаёт pending-запись в ACCESS_CONTROL; уже существующая запись не повышает роль. В `/help` команда показана как HTML `<code>/my_status</code>`, чтобы подчёркивание не терялось.

## Результат
Harness: public, отсутствие строки реестра, смена username, пустой/ошибочный lookup, public help, сохранность underscore и отсутствие утечки чужих данных — PASS.
