import pandas as pd

courses = ["eos240", "eos408", "eos423"]
for c in courses:
    prefix = f"source/{c}-public/"
    df = pd.read_csv(
        f"{prefix}Outline/tables/schedule.csv",
        names=["week", "day", "mon", "date", "color", "activity", "topic", "reading"],
    )
    df = df.fillna("")

    cmap = {}
    cmap["myblue"] = "#3D4F7D"
    cmap["myred"] = "#CD4F38"
    cmap["mygreen"] = "#657060"
    cmap["myorange"] = "#E48C2A"
    cmap["mygreen2"] = "#44A57C"
    cmap["myskyblue"] = "#64b5cd"

    lines = ""
    for row in df.iterrows():
        color = str(cmap[row[1]["color"]])
        week = row[1]["week"]
        if type(week) is str:
            week = week
        else:
            week = f"{week:0.0f}"
        dayn = row[1]["date"]
        if type(dayn) is str:
            dayn = dayn
        else:
            dayn = f"{dayn:0.0f}"
        date = f"{row[1]['day']} {row[1]['mon']} {dayn}"
        top1 = row[1]["activity"]
        top2 = row[1]["topic"]
        top2 = top2.replace("\emph{", "<i>")
        top2 = top2.replace("}", "</i>")
        line = f"""<div style="text-align:center">{week}</div>
        <div style="text-align:right">{date}</div>
        <div style="text-align:left"><span style='color:{color}'>{top1}</span></div>
        <div style="text-align:right"><span style='color:{color}'>{top2}</span></div>
        """
        lines += line

    table = f"""<div style="display: grid;grid-column-gap: 10px;
    grid-template-columns: 6% 10% 22% 52%;font-weight:bold">
    <div style="text-align:center">Week</div>
    <div style="text-align:right">Date</div>
    <div style="text-align:left"> </div>
    <div style="text-align:right">Topic</div>
    {lines}
    </div>
    """

    with open(f"{prefix}Outline/html/calendar.html", "w+") as f:
        f.writelines(table)

    df = pd.read_csv(f"{prefix}Outline/tables/learning_outcomes.csv", names=["outcome"])
    lines = ""
    for row in df.iterrows():
        outcome = row[1]["outcome"]
        line = f"""<li>{outcome}</li>
        """
        lines += line

    table = f"""<ul>
    {lines}
    </ul>
    """

    with open(f"{prefix}Outline/html/learning_outcomes.html", "w+") as f:
        f.writelines(table)