# import stuff and compute data df...

from scipy import stats

# get coeffs of linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(data['years'], np.log10(data['salary']))

data_logged = data.copy()
data_logged['salary'] = np.log10(data['salary'])

# ax.set_yscale('log')  # set_yscale is a function, not a string

# use line_kws to set line label for legend

fs = (15, 8.27)
fig, ax = plt.subplots(figsize=fs)
sns.regplot("years", "salary", data=data, color='#3D9977', ax=ax, fit_reg=False,)

#ax.set_yscale('log')
plt.plot(np.linspace(0, 40), 10**(intercept + slope*np.linspace(0, 40)), color='#3D9977',
            label="salary = {1:.0f} * {0:.3f}^years".format(10.0**slope, 10.0**intercept))

ax.set_xlim([-0.5, 40])
ax.set_ylim([0, 210000])

ax.legend()

plt.title('Linear regression -> procentuell lönepåverkan')

# R2 computed on linear scale
r_value = 1.0 - (data.salary - 10**(intercept + slope*data.years)).std()**2/data.salary.std()**2

print("R2 = {:.2f}".format(r_value))
print("p = {:}".format(p_value))

plt.show()

