# задача определение четности числа
определение четности числа

## выбор решения:
Реализовано 3 способа решения данной задачи (один из них представлен в условии). С целью проверки обоснованности выбранных решений осуществляется замер времени на каждый варинт решения. 
При запуске видно, что наиболее эффективный вариант использование побитового '&'. 
Причина: из трех вариантов побитовое & точно выполняет на каждом шаге одну операцию '&', в отличии от двух смещений '>> <<', или варианта представленного  в условии задачи.

## Как запустить:
Запустить файл :

```
проверка четности.py
```

# задача циклического буфера FIFO
задача циклического буфера FIFO

## выбор решения:
Реализовано 2 способа решения задачи. Перевый на базе списка. Основным недостатком является сложность удаления элемента из списка, т.к. потребуется проитись по все оставшимся элементам и сдвинуть их на 1 элемент. При запуске будет выведено время добавления и удаления 10000 элементов.

Второй на базе класса циклической очереди. Данный метод решен проблемы первого и более предпочителен. 

Общая проблема для циклических очередей ограничение по количеству элементов. 

## Как запустить:
Запустить файл :

```
очередь на базе списка.py
```

```
кольцевая очередь.py
```
# задача сортировки
задача сортировки

## выбор решения:
Задача решена алгоритмом быстрой сортировкиб т.к.к алгоритм показывает наилучшие результаты в случае наиболее рандомного размещения в массиве элементов.

## Как запустить:
Запустить файл :

```
быстрая сортировка.py
```
