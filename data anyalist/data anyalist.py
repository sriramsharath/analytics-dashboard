# Import libraries
from matplotlib import pyplot as plt

  
# Creating dataset
food_items = ['BIRIYANI', 'CHINESE FAST FOOD', 'KFC',
        'ICE CREAM', 'STARTERS', 'PIZZA','OTHERS']  
  
data = [59, 56, 69, 22, 30, 58,10]

# Creating plot
fig = plt.figure(figsize =(10,7))
plt.pie(data, labels = food_items)
plt.title('FAMILYRESTAURANT SALES PIE CHART PER DAY')
  
# show plot
plt.show()