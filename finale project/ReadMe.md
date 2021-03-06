# Финальный проект

Предсказание стоимости домов, основываясь на истории предложений.



## Задача

Ко мне обратился представитель крупного агентства недвижимости со следующей проблемой:

"Мои риелторы тратят катастрофически много времени на сортировку объявлений и поиск выгодных предложений. Поэтому их скорость реакции, да и, сказать по правде, качество анализа не дотягивает до уровня конкурентов. А это сказывается на наших финансовых показателях. Твоя задача — разработать модель, которая бы позволила обойти конкурентов по скорости и качеству совершения сделок. Датасет прикладываю."

### Цель: разработать сервис, который будет предсказывать стоимость домов, основываясь на истории предложений.
### Этапы работы над проектом:

1) Первичная обработка данных;
1) EDA (анализ распределения признаков и замена пропусков);
3) Features Engineering;
4) Корреляционный анализ;
5) Нормирование признаков - Scaling;
6) Построение моделей

## Выводы:

В результате EDA было создано много новых признаков, а также почищены выбросы, пропуски и плохие значения. Как итог мы получили хороший датасет, на котором модели показывают хорошие результаты.

Основной метрикой MAE и MAPE, так как первая показывает средний модуль отклонения, а вторая средний процент отклонения от цены.
Во время разработки модели машинного обучения было опробовано несколько методов и выбран лучший, к которому в итоге дополнительно подобрали гиперпараметры.
### Модели:

#### Примитивная модель
MAE: 176432.46$
MAPE: 1.2%
R2: -0.0%

#### Линейная регрессия
MAE: 187555.26$
MAPE: 0.95%
R2: -0.2%
Линейная регрессия оказалась даже хуже, чем "предсказание среднего"

#### Случайный лес
MAE: 67006.56$
MAPE: 0.3%
R2: 0.79%
Метрики стали в разы лучше у нелинейной модели.

#### Light Gradient Boosting
MAE: 86015.8$
MAPE: 0.4%
R2: 0.72%
Метрики значительно хуже, чем у случайного леса.

#### Extreme Gradient Boosting
MAE: 76241.7$
MAPE: 0.34%
R2: 0.77%
Результат чуть лучше, чем у LGBM, но все равно сильно хуже, чем у RF.
Как итог, решили настроить RF.
После перебора гиперпараметров были выявлены слудующие значения параметров.

n_estimators = 700
max_depth = 70
max_features = 29

И метрики улучшились больше, чем на 2000$:
MAE: 65880.05$
MAPE: 0.29%
R2: 0.8%

Итоговая модель практически в 3 раза точней (по метрике МАЕ), чем примитивное предсказание. Я считаю, что это отличный результат.


