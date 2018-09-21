# import stuff and compute data df...

from scipy import stats

fs = (15, 8.27)
fig, ax = plt.subplots(figsize=fs)

# get coeffs of linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(data['years'], data['salary'])

# use line_kws to set line label for legend
ax = sns.regplot(x="years", y="salary", data=data, color='#3D9977',
 line_kws={'label':"salary = {0:.0f} * years + {1:.0f}".format(slope, intercept)})

# plot legend
ax.legend()
plt.title('Linjär regression')

print("R2 = {:.2f}".format(r_value))
print("p = {}".format(p_value))

plt.show()
