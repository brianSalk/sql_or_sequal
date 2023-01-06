import matplotlib.pyplot as plt
def create_sql_vs_sequal_chart(sql_dict):
    plt.bar(sql_dict.keys(), sql_dict.values())
    plt.title('SQL vs. Sequal')
    plt.show()
    plt.label(['SQL','Sequal'])
