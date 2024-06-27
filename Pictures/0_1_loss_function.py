plt.figure(figsize=(4,3))
font = {'size'   : 12, "weight" : 'normal'}

plt.rc('font', **font)
plt.plot([0,0.5,0.5,1],[0,0,1,1], label="y_t = 0")
plt.plot([0,0.5,0.5,1],[1,1,0,0], label="y_t = 1")
plt.yticks([0,1],[0,1])
plt.xticks([0,0.5,1],[0,0.5,1])
plt.xlabel('ŷ_t')
plt.ylabel('loss')
plt.title("0/1 loss function")
plt.legend()
plt.tight_layout()
