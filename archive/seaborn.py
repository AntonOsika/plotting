fig = plt.figure(figsize=[10, 8])
df2 = pd.melt(df, id_vars="course_name", var_name="index", value_name="y")
sns.factorplot(x='course_name', y='y', hue='index', data=df2, kind='bar', ax=plt.gca())
plt.xticks(rotation=30, ha='right')
