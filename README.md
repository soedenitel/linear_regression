# Курс Машинное обучение 1: линейная регрессия
## Рассчитать данные по энергопотреблению
### Описание задания
Загрузите данные и посчитайте модели линейной регрессии для 50 зданий по ансамблю регрессионных моделей:
* в первой модели весь оптимальный набор метеорологических данных,
* во второй - дни недели и праздники,
* в третьей - недели года,
* в четвертой - месяцы.

Финальное значение показателя рассчитайте как взвешенное арифметическое среднее показателей всех моделей, взяв веса для первой и второй модели как 3/8, а для третьей и четвертой - как 1/8.

Загрузите данные решения, посчитайте значение энергопотребления для требуемых дат для тех зданий, которые посчитаны в модели, и выгрузите результат в виде CSV-файла (submission.csv).

Данные:
* http://video.ittensive.com/machine-learning/ashrae/building_metadata.csv.gz
* http://video.ittensive.com/machine-learning/ashrae/weather_train.csv.gz
* http://video.ittensive.com/machine-learning/ashrae/train.0.csv.gz
* http://video.ittensive.com/machine-learning/ashrae/test.csv.gz
* http://video.ittensive.com/machine-learning/ashrae/weather_test.csv.gz

### Выполнение задания
1. [Определение фактических параметров задания](homework.ipynb#task_definition)
2. [ETL](homework.ipynb#etl)
3. [Построение для каждого типа (набора признаков) моделей линейной регрессии](homework.ipynb#modelling)
4. [Построение прогнозов для каждого типа моделей](homework.ipynb#prediction)
5. [Вычисление финального значения как взвешенного арифметического среднего](homework.ipynb#result)
6. [Формирование выгрузки данных для тех зданий, которые посчитаны в модели](homework.ipynb#create_submision)
7. [Выгрузка результат в виде CSV-файла (submission.csv)](homework.ipynb#save_submision)