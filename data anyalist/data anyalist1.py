# Import libraries

import matplotlib.pyplot as plt
  
  
# Creating dataset
food_items = ['BIRYANI', 'CHINESE FAST FOOD', 'KFC', 
        'ICE CREAM', 'STARTERS', 'PIZZA','OTHERS']
  
data = [59, 56, 69, 22, 30, 58,10]
  
  
# Creating explode data
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1,0.1)
  
# Creating color parameters
colors = ( "orange", "cyan", "white",
          "grey", "indigo", "beige","yellow")
  
# Wedge properties
wp = { 'linewidth' : 2, 'edgecolor' : "BLACK" }
  
# Creating autocpt arguments
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} ORDERS)".format(pct, absolute)
  
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data, 
                                  autopct = lambda pct: func(pct, data),
                                  explode = explode, 
                                  labels = food_items,
                                  shadow = False,
                                  colors = colors,
                                  startangle = 90,
                                  wedgeprops = wp,
                                  textprops = dict(color ="RED"))
  
# Adding legend
ax.legend(wedges, food_items,
          title ="FAMILY RESTAURANT",
          loc ="upper left",
          bbox_to_anchor =(1, 0, 0.5, 1))
  
plt.setp(autotexts, size = 10, weight ="bold")
ax.set_title("FAMILY RESTAURANT SALES 0N NEW YEAR 2021")
  
# show plot
plt.show()