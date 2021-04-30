# Rukhlyada-Rukhlyada-Nadya_and_Katya.Spectral_properties_of_graphs

##Техническая библиотека: коллекция алгоритмов на графах, основанных на спектральных свойствах

Алгебр теория графов 

Постановка задачи: у нас есть матрица смежности графа, подаем ее на вход (nxn). Мы проверить его спектральные свойства, а именно: 

1) Найти характеристический полином графа 

Для данной матрицы $ A $, $ \chi (\lambda )=\det(A-\lambda E) $, где $ E $ — единичная матрица, является многочленом от $ \lambda $, который называется характеристическим многочленом матрицы $ A $.

Ценность характеристического многочлена в том, что собственные значения матрицы являются его корнями. Действительно, если уравнение $ Av=\lambda v $ имеет ненулевое решение, то $ (A-\lambda E)v=0 $, значит матрица $ A-\lambda E $ вырождена и её определитель $ \det(A-\lambda E)=\chi (\lambda ) $ равен нулю.

Связанные определения:

Матрицу $ A-\lambda E $ называют характеристической матрицей матрицы $ A $.

Уравнение $ \chi (\lambda )=0 $ называют характеристическим уравнением матрицы $ A $.

Характеристический многочлен графа — это характеристический многочлен его матрицы смежности.

Найти собственные значения графа 
Найти собственные вектора графа 
Построение инварианта Колена де Вардьера ??? понять? если поймем и это быстро, то еще критерии из презентации (4 слайд) 
Проверка на двудольность (27 слайд) 
Проверка на целосчисленность 
Проверка на наличие треугольников в графе (12 слайд) 
Поиск числа независимости k-регулярного графа с помощью неравенства Хоффмана-Дельсарта 
Построение матрицы Лапласа 
Построение беззнаковой матрицы Лапласа *Реализована возможность отрисовки графа по его матрице смежности
