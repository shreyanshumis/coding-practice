from matplotlib import pyplot as plt

Age = [15,16,14,10]
Class = [10,11,9,4]
plt.plot(Age, Class, marker='*')
plt.title("Information")
plt.ylabel('Age')
plt.xlabel('Class')
plt.show()