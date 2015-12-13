import plotly.plotly as py
from plotly.graph_objs import *
from pydblite import Base
year = []
lst_jungwat = []
lst_death = []
db = Base('Thai-db.pdl')
db.open()
for i in db('ปี'): #ใส่ปีใน li
    if i['ปี'] in year:
        break
    else:
        year.append(i['ปี'])
for i in db('จังหวัด'): #ใส่จังหวัดใน list
    if i['จังหวัด'] in lst_jungwat:
        pass
    else:
        lst_jungwat.append(i['จังหวัด'])
i = 0
def change_death(j):
    for i in db('จังหวัด') == lst_jungwat[j]:
        lst_death.append(i['ตาย'])
"""-----------------------------------------------"""
change_death(i)
trace1 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(0, 0, 0)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace2 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(119, 136, 153)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""

i += 1
lst_death = []
change_death(i)
trace3 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(198, 226, 255)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace4 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(151, 255, 255)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace5 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(238, 232, 170)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace6 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(139, 69, 19)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace7 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(205, 133, 63)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace8 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(244, 164, 96)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace9 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(255, 218, 185)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace10 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(238, 207, 161)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace11 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(205, 201, 165)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace12 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(139, 136, 120)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace13 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(132, 112, 255)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace14 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(71, 60, 139)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace15 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(72, 118, 255)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace16 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(39, 64, 139)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace17 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(0, 0, 255)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace18 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(25, 25, 112)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace19 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(176, 224, 230)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace20 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(24, 116, 205)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace21 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(0, 154, 205)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace22 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(74, 112, 139)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace23 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(95, 158, 160)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace24 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(150, 205, 205)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace25 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(0, 206, 209)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace26 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(0, 245, 255)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace27 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(102, 205, 170)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace28 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(46, 139, 87)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace29 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(0, 139, 69)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace30 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(0, 255, 0)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace31 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(0, 100, 0)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace32 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(32, 178, 170)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace33 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(0, 250, 154)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace34 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(107, 142, 35)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace35 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(202, 255, 112)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace36 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(255, 246, 143)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace37 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(139, 134, 78)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace38 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(255, 255, 0)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace39 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(139, 139, 0)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace40 = Scatter(
    x=[2554, 2555, 2556, 2557],
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(205, 173, 0)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace41 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(139, 101, 8)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace42 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(188, 143, 143)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace43 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(255, 193, 193)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_birth = []
change_death(i)
trace44 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(205, 92, 92)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace45 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(255, 130, 71)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace46 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(139, 71, 38)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace47 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(139, 115, 85)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace48 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(205, 133, 63)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace49 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(255, 127, 36)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace50 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(205, 38, 38)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace51 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(255, 20, 147)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace52 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(139, 10, 80)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace53 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(205, 96, 144)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace54 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(139, 99, 108)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace55 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(176, 48, 96)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace56 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(205, 0, 205)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace57 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(139, 0, 139)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace58 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(186, 85, 211)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace59 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(148, 0, 211)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace60 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(128, 0, 128)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace61 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(236, 171, 83)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace62 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(192, 192, 192)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace63 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(0, 128, 128)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace64 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(255, 204, 153)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace65 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(142, 124, 195)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace66 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(0, 154, 205)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace67 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(238, 59, 59)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace68 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(50, 205, 50)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace69 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(34, 139, 34)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace70 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(105, 139, 34)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace71 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(205, 173, 0)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace72 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(0, 154, 205)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace73 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(155, 205, 155)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace74 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(46, 139, 87)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace75 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(192, 255, 62)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""
i += 1
lst_death = []
change_death(i)
trace76 = Scatter(
    x=year,
    y=lst_death,
    connectgaps=True,
    line=Line(
        color='rgb(95, 158, 160)',
        width=1
    ),
    name=lst_jungwat[i],
    uid='dd3a3c'
)
"""-----------------------------------------------"""


data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18, trace19, trace20, trace21\
             , trace22, trace23, trace24, trace25, trace26, trace27, trace28, trace29, trace30, trace31, trace32, trace33, trace34, trace35, trace36, trace37, trace38, trace39, trace40\
             ,trace41, trace42, trace43, trace44, trace45, trace46, trace47, trace48, trace49, trace50, trace51, trace52, trace53, trace54, trace55, trace56, trace57, trace58, trace59\
             , trace60, trace61, trace62, trace63, trace64, trace65, trace66, trace67, trace68, trace69, trace70, trace71, trace72, trace73, trace74, trace75, trace76])
layout = Layout(
    autosize=True,
    bargap=0.2,
    bargroupgap=0,
    barmode='stack',
    boxgap=0.3,
    boxgroupgap=0.3,
    boxmode='overlay',
    dragmode='zoom',
    font=Font(
        color='rgb(33, 33, 33)',
        family='"Old Standard TT", serif',
        size=12
    ),
    height=600,
    hidesources=False,
    hovermode='x',
    legend=Legend(
        x=0.01788617886178862,
        y=1.0166666666666666,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(0, 0, 0, 0)',
        borderwidth=1,
        font=Font(
            color='rgb(33, 33, 33)',
            family='',
            size=0
        ),
        traceorder='normal',
        xanchor='auto',
        yanchor='auto'
    ),
    margin=Margin(
        r=80,
        t=100,
        autoexpand=True,
        b=80,
        l=80,
        pad=2
    ),
    paper_bgcolor='#fff',
    plot_bgcolor='#fff',
    separators='.,',
    showlegend=False,
    smith=False,
    title='กราฟแสดงจำนวนการเกิดของประเทศไทย ปี 2548-2557',
    titlefont=dict(
        color='',
        family='',
        size=0
    ),
    width=775,
    xaxis=XAxis(
        anchor='y',
        autorange=True,
        autotick=True,
        domain=[0, 1],
        dtick='M12.000000000000002',
        exponentformat='e',
        gridcolor='#ddd',
        gridwidth=1,
        linecolor='rgb(221, 221, 221)',
        linewidth=1,
        mirror=False,
        nticks=15,
        overlaying=False,
        position=0,
        range=[1046754000000, 1378008000000],
        rangemode='normal',
        showexponent='all',
        showgrid=False,
        showline=True,
        showticklabels=True,
        tick0=946702800000,
        tickangle='auto',
        tickcolor='#000',
        tickfont=dict(
            color='',
            family='',
            size=0
        ),
        ticklen=5,
        ticks='',
        tickwidth=1,
        title='<i>ปี</i>',
        titlefont=dict(
            color='',
            family='',
            size=0
        ),
        type='year',
        zeroline=False,
        zerolinecolor='#000',
        zerolinewidth=1
    ),
    yaxis=YAxis(
        anchor='x',
        autorange=False,
        autotick=True,
        domain=[0, 1],
        dtick=100,
        ##exponentformat='e',
        gridcolor='#ddd',
        gridwidth=1,
        linecolor='rgb(221, 221, 221)',
        linewidth=1,
        mirror=False,
        nticks=0,
        overlaying=False,
        position=0,
        range=[0, 50000],
        rangemode='normal',
        ##showexponent='all',
        showgrid=True,
        showline=True,
        showticklabels=True,
        tick0=0,
        tickangle='auto',
        tickcolor='#000',
        tickfont=dict(
            color='',
            family='',
            size=0
        ),
        ticklen=5,
        ticks='',
        tickwidth=1,
        title='จำนวนการเกิด',
        titlefont=dict(
            color='',
            family='',
            size=0
        ),
        type='linear',
        zeroline=False,
        zerolinecolor='#000',
        zerolinewidth=1
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
