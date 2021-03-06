""" The graph shows the number of summary of birth and death since 2548 to 2557. """
import plotly.plotly as py
from plotly.graph_objs import *
from pydblite import Base
db = Base('Thai-db.pdl')
db.open()
def make_data():
    """ make list of summary of birth and death each year. """
    year = []
    lst_birth = []
    lst_death = []
    birth_2548 = 0
    death_2548 = 0
    birth_2549 = 0
    death_2549 = 0
    birth_2550 = 0
    death_2550 = 0
    birth_2551 = 0
    death_2551 = 0
    birth_2552 = 0
    death_2552 = 0
    birth_2553 = 0
    death_2553 = 0
    birth_2554 = 0
    death_2554 = 0
    birth_2555 = 0
    death_2555 = 0
    birth_2556 = 0
    death_2556 = 0
    birth_2557 = 0
    death_2557 = 0
    for i in db('ปี'):
        if i['ปี'] == 2548:
            birth_2548 += (i['เกิด'])
            death_2548 += (i['ตาย'])
        elif i['ปี'] == 2549:
            birth_2549 += (i['เกิด'])
            death_2549 += (i['ตาย'])
        elif i['ปี'] == 2550:
            birth_2550 += (i['เกิด'])
            death_2550 += (i['ตาย'])
        elif i['ปี'] == 2551:
            birth_2551 += (i['เกิด'])
            death_2551 += (i['ตาย'])
        elif i['ปี'] == 2552:
            birth_2552 += (i['เกิด'])
            death_2552 += (i['ตาย'])
        elif i['ปี'] == 2553:
            birth_2553 += (i['เกิด'])
            death_2553 += (i['ตาย'])
        elif i['ปี'] == 2554:
            birth_2554 += (i['เกิด'])
            death_2554 += (i['ตาย'])
        elif i['ปี'] == 2555:
            birth_2555 += (i['เกิด'])
            death_2555 += (i['ตาย'])
        elif i['ปี'] == 2556:
            birth_2556 += (i['เกิด'])
            death_2556 += (i['ตาย'])
        elif i['ปี'] == 2557:
            birth_2557 += (i['เกิด'])
            death_2557 += (i['ตาย'])
    lst_birth = [birth_2548, birth_2549, birth_2550, birth_2551, birth_2552,
                     birth_2553, birth_2554, birth_2555, birth_2556, birth_2557]
    lst_death = [death_2548, death_2549, death_2550, death_2551, death_2552,
                     death_2553, death_2554, death_2555, death_2556, death_2557]
    return lst_birth, lst_death

def make_list_year(db, year=[]):
    """ make list of year """
    for i in db('ปี'): #ใส่ปีใน list
        if i['ปี'] in year:
            break
        else:
            year.append(i['ปี'])
    return year

def make_graph():
    """ make graph from data """
    make_data()
    year = make_list_year(db)
    lst_birth = make_data()[0]
    lst_death = make_data()[1]
    trace1 = Bar(
        x=year,
        y=lst_birth,
        marker=Marker(
            color='rgb(222, 113, 88)'
        ),
        name='birth',
        uid='368324'
    )
    trace2 = Bar(
        x=year,
        y=lst_death,
        marker=Marker(
            color='rgb(84, 172, 234)'
        ),
        name='death',
        uid='25a4e9'
    )
    data = Data([trace1, trace2])
    layout = Layout(
        annotations=Annotations([
            Annotation(
                x=0.1000000000000038,
                y=0.5709595420143821,
                align='center',
                arrowcolor='rgba(0, 0, 0, 0)',
                arrowhead=1,
                arrowsize=1,
                arrowwidth=0,
                ax=436,
                ay=155.98332977294922,
                bgcolor='rgba(0,0,0,0)',
                bordercolor='',
                borderpad=1,
                borderwidth=1,
                font=Font(
                    color='',
                    family='',
                    size=0
                ),
                opacity=1,
                showarrow=True,
                text='Source: <a href="http://qz.com/187350/six-charts-that-show-why-china-is-competing-with-the-multinationals-it-used-to-work-for/">Quartz</a>',
                xanchor='auto',
                xref='paper',
                yanchor='auto',
                yref='paper'
            )
        ]),
        autosize=False,
        bargap=0.1,
        bargroupgap=0.15,
        barmode='group',
        boxgap=0.3,
        boxgroupgap=0.3,
        boxmode='overlay',
        dragmode='zoom',
        font=Font(
            color='rgb(33, 33, 33)',
            family="'Open sans', verdana, arial, sans-serif",
            size=12
        ),
        height=400,
        hidesources=False,
        hovermode='x',
        legend=Legend(
            x=0.001851851851851852,
            y=0.9863636363636363,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(0, 0, 0, 0)',
            borderwidth=1,
            font=Font(
                color='',
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
            pad=0
        ),
        paper_bgcolor='#fff',
        plot_bgcolor='#fff',
        separators='.,',
        showlegend=True,
        smith=False,
        title='<br> The graph shows the number of summary of birth and death since 2548 to 2557 .',
        titlefont=dict(
            color='',
            family='',
            size=0
        ),
        width=700,
        xaxis=XAxis(
            anchor='y',
            autorange=True,
            autotick=True,
            domain=[0, 1],
            dtick=1,
            #exponentformat='e',
            gridcolor='#ddd',
            gridwidth=1,
            linecolor='#000',
            linewidth=1,
            mirror=False,
            nticks=17,
            overlaying=False,
            position=0,
            range=[2548, 2557],
            rangemode='normal',
            #showexponent='all',
            showgrid=False,
            showline=True,
            showticklabels=True,
            tick0=2001,
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
            title="<i>year</i>",
            titlefont=dict(
                color='',
                family='',
                size=0
            ),
            type='linear',
            zeroline=False,
            zerolinecolor='#000',
            zerolinewidth=1
        ),
        yaxis=YAxis(
            anchor='x',
            autorange=False,
            autotick=True,
            domain=[0, 1],
            dtick=2,
            #exponentformat='e',
            gridcolor='#ddd',
            gridwidth=1,
            linecolor='#000',
            linewidth=1,
            mirror=False,
            nticks=0,
            overlaying=False,
            position=0,
            range=[200000, 950000],
            rangemode='normal',
            #showexponent='all',
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
            title='summary of birth and death',
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

make_graph()
