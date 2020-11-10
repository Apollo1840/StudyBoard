from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

from constant import *


def duration_in_mins(t_start, t_end):
    t_start = datetime.strptime(str(t_start), "%H:%M")
    t_end = datetime.strptime(str(t_end), "%H:%M")
    return (t_end - t_start).seconds / 60


def min2duration_str(minutes):
    duration_str = ""
    hour = int(minutes//60)
    min = int(minutes % 60)

    if hour != 0:
        if hour == 1:
            duration_str += "1 hour"
        else:
            duration_str += "{} hours".format(hour)

    if min != 0:
        duration_str += " {} minutes".format(min)

    return duration_str


def plot_the_bar_chart(df, output_path="sample.png"):
    df[MINUTES] = [duration_in_mins(t_start, t_end) for t_start, t_end in zip(df[START_TIME], df[END_TIME])]
    df_r = df.groupby(NAME)[MINUTES].apply(sum)
    df_r = df_r.reset_index()
    df_r = df_r.sort_values(by=MINUTES, ascending=False)

    sns.set_style("darkgrid")
    fig = plt.figure(figsize=(10, 10))
    sns.barplot(data=df_r, y=df_r[NAME], x=df_r[MINUTES])
    plt.title("The study time of the candidates (in minutes)")
    fig.savefig(output_path)

    return df_r


