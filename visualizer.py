import matplotlib.pyplot as plt

def plot_bar(data, title, xlabel, ylabel, color='skyblue', horizontal=False):
    
    plt.figure(figsize=(10, 6))
    if horizontal:
        data.plot(kind='barh', color=color)
    else:
        data.plot(kind='bar', color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_hist(data, title, xlabel, ylabel, color='green'):
   
    plt.figure(figsize=(8, 5))
    data.hist(bins=20, color=color, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(False)
    plt.tight_layout()
    plt.show()

def plot_scatter(x, y, title, xlabel, ylabel, color='red'):
   
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, alpha=0.3, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()
