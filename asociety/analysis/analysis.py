

from asociety.repository.database import engine
import pandas as pd


def judge(row):
    agent_answer = row['agent_answer']
    right_answer = row['answer']
    if(agent_answer == right_answer):
        return 100.0
    return 0.0
    pass
class ExperimentSummary:
    def __init__(self, experiment_name) -> None:
        self.df = pd.read_sql_query("select * from qa_view where experiment_name = '" + experiment_name + "'", engine)
    
    def statistics(self, column):
        self.df["result"] = self.df.apply(judge, axis='columns')
        d = {'result':'average'}
        df=self.df.groupby(column).agg({'result':'mean'}).rename(columns=d)
        return df

    def create_matplotlib(self):
            """创建绘图对象"""
            # 设置中文显示字体
            mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
            mpl.rcParams['axes.unicode_minus'] = False  # 负号显示
            # 创建绘图对象f figsize的单位是英寸 像素 = 英寸*分辨率
            self.figure = plt.figure(num=2, figsize=(7, 4), dpi=80, facecolor="gold", edgecolor='green', frameon=True)
            self.figure.text(0.45, 0.94, '这是柱状图图') # 设置显示的文本
            x = np.arange(12)
            y = np.random.uniform(0.5, 1.0, 12) * (1 - x / float(12))
            loc = zip(x, y)  # 将x, y 两两配对
            plt.ylim(0, 1.2)  # 设置y轴的范围
            plt.bar(x, y, facecolor='green', edgecolor='black')  # 绘制柱状图(填充颜色绿色，边框黑色)
            for x, y in loc:
                plt.text(x + 0.1, y + 0.01, '%.2f' % y, ha='center', va='bottom')  # 保留小数点2位
       

if __name__ == "__main__":
    e = ExperimentSummary('ddd')
    e.statistics('sex')