\Завдання 1 

# Встановлення бібліотеки PuLP (якщо не встановлена)
# !pip install pulp
import pulp
def optimize_production():
    # Створення проблеми лінійного програмування
    prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)
    # Визначення змінних
    limonade = pulp.LpVariable('Limonade', lowBound=0, cat='Continuous')
    fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')
    # Додавання обмежень на ресурси
    prob += 2 * limonade + fruit_juice <= 100, "Water"
    prob += limonade <= 50, "Sugar"
    prob += limonade <= 30, "LemonJuice"
    prob += 2 * fruit_juice <= 40, "FruitPuree"
    # Цільова функція - максимізація кількості вироблених продуктів
    prob += limonade + fruit_juice, "TotalProduction"
    # Розв'язання задачі
    prob.solve()
    # Виведення результатів
    print(f"Status: {pulp.LpStatus[prob.status]}")
    print(f"Кількість виробленого лимонаду: {pulp.value(limonade)}")
    print(f"Кількість виробленого фруктового соку: {pulp.value(fruit_juice)}")
    print(f"Загальна кількість вироблених продуктів: {pulp.value(prob.objective)}")
if __name__ == "__main__":
    optimize_production()





\Завдання 2 
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
# Визначення функції та межі інтегрування
def f(x):
    return x ** 2
a = 0  # Нижня межа
b = 2  # Верхня межа
# Метод Монте-Карло
N = 10000
x_random = np.random.uniform(a, b, N)
y_random = f(x_random)
integral_mc = (b - a) * np.mean(y_random)
print(f"Інтеграл методом Монте-Карло: {integral_mc}")
# Метод Quad з SciPy
result, error = spi.quad(f, a, b)
print("Інтеграл (quad): ", result)
# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show() 



### Висновки 
# Порівняльний аналіз результатів
## Метод Монте-Карло
Інтеграл, обчислений методом Монте-Карло: 2.675336
## Метод Quad з SciPy
Інтеграл, обчислений за допомогою функції `quad`: 2.666666666666667
## Висновки
Як видно з порівняння, метод Монте-Карло дає результат, близький до аналітично обчисленого інтеграла з використанням функції `quad`. Незважаючи на те, що метод Монте-Карло є статистичним і може давати деякі відхилення від точного значення, він показує себе як ефективний інструмент для приблизного обчислення інтегралів, особливо коли аналітичний метод складний або неможливий.
Оцінка абсолютної помилки, надана функцією `quad`, також підтверджує високу точність отриманого результату.
