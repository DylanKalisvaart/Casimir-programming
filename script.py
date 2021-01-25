import test
import matplotlib.pyplot as plt

print('some print statement')

r = 2
circumference = test.circumference_circle(r)
area = test.area_circle(r)

print('Circumference: ', circumference)
print('Area: ', area)

r = 2
fig, ax = test.plot_circle(r)
plt.savefig('circle.png')
