# Запуск

### Windows:

```
python -m venv .venv
```

```
.\.venv\Scripts\activate.bat
```

```
pip install -r .\requirements.txt
```


```
python .\kurs_system_modelling\AppUi.py
```

# Задание
```
Распределенный банк данных системы сбора информации организован на базе компьютеров, соединенных дуплексным каналом связи. 
Поступающий запрос обрабатывается на первом компьютере и с вероятностью 50% необходимая информация обнаруживается на месте. 
В противном случае необходима посылка запроса во второй компьютер. Запросы поступают через 10±3 с, 
первичная обработка запроса занимает 2 с, выдача ответа требует 18±2 с, передача по каналу связи занимает 3 с. 
Временные характеристики второго компьютера аналогичны первой. 

Смоделировать прохождение 400 запросов. Определить необходимую емкость накопителей перед компьютером, обеспечивающую безотказную работу системы, и функцию распределения времени обслуживания заявки.
```
