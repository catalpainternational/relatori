import sys
import cairo
import pycha.pie
import pycha.bar

from catalpa.relatori import models
from catalpa.relatori.report import * 


def pie_chart(name, dataset, width=350, height=300, options=None ):
    """
    usage:
    >>> dataset = [
            ('ermera', [[0, 40]]),
            ('hatolia', [[0, 30]]),
            ('letefoho', [[0, 20]]),
            ]
    >>> pie_chart('charts/pie_example.png', dataset)
    """
    
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    if options == None:
        options = {
            'background': {
                'chartColor': '#ffffff',
                'baseColor': '#ffffff',
                'lineColor': '#0f0f0f'
            },
            'legend': {
                'hide': True,
            },
            'title': None,
        }
    chart = pycha.pie.PieChart(surface, options)
    chart.addDataset(dataset)
    chart.render()
    surface.write_to_png(name)


def vertical_bar_chart(name, dataset, width=700, height=200, x_ticks=None, y_ticks=None, options=None ):
    """
    usage:
    >>> dataset = [
            ('ermera', [[0, 40]]),
            ('hatolia', [[0, 30]]),
            ('letefoho', [[0, 20]]),
            ]    
    >>> vertical_bar_chart('vertical_bar_example.png', dataset)
    """

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    if options == None:    # if no options passed lets set some not-so-sensible defaults
        if y_ticks == None:
            y_ticks = [dict(v=20, label='20'),
                        dict(v=40, label='40'),
                        dict(v=60, label='60'),
                        dict(v=80, label='80'),
                        dict(v=100, label='100')]
        options = {
            'axis': {
                'labelFont' : 'Helvetica',
                'labelFontSize' : 10,
                'tickFont' : 'Helvetica',
                'tickFontSize' : 12,
                'x': {
                    'hide' : False,
                    'label': None,
                    'rotate': 0,
                    'ticks': x_ticks,
    
                },
                'y': {
                    'ticks': y_ticks,
                    'tickCount' : 4,
                    'tickPrecision': 0,
                    'label' : None,
                    'range' : (0,100),
                }
            },
            'background': {
                'chartColor': '#ffffff',
                'baseColor': '#ffffff',
                'lineColor': '#0f0f0f'
            },
            'colorScheme': {
                'name': 'gradient',
                'args': {
                    'initialColor': 'green',
                },
            },
            'legend': {'borderColor': '#0f0f0f',
                    'borderWidth': 0,
                    'hide': False,
                    'opacity': 0.50,
                    'position': {'bottom': None,
                                 'left': None,
                                 'right': 20,
                                 'top': 10}},
                    'padding': {
                        'left': 10,
                        'bottom': 10,
                        'right' : 100,
                    },
            'title': None,
        }
    chart = pycha.bar.VerticalBarChart(surface, options)
    chart.addDataset(dataset)
    chart.render()
    surface.write_to_png(name)


def pie_chart_by_name(name, parent):
    """
    Given a string 'name' and a parent of HealthFacility
    """
    indicator_type = models.IndicatorType.objects.filter(name__icontains=name)[0]
    pie_chart("relatori/static/images/tmp/%s.png" % indicator_type.name, indicator_by_type(parent, indicator_type))


def chart_by_name(name, parent):
    """
    usage:
    >>> chart_by_names(('k1','k4'), parent)
    """
    indicator_type = models.IndicatorType.objects.filter(name__icontains=name)[0]
    x_ticks = []
    column = 0
    for child in parent.children:
        x_ticks.append(dict(v=column, label=child.name))
        column += 1
    x_ticks.append(dict(v=column, label=parent.name+' Average'))
    vertical_bar_chart("relatori/static/images/tmp/%s.png" % name, indicators_by_parent_by_type(parent, indicator_type), x_ticks = x_ticks)


def chart_by_names(names, parent):
    """
    Given a list of names (words) in IndicatorType names and an parent area
    Print stats per facility or sub-area
    return a list containting stats per facility per IndicatorType to be consumed by pycha
    Usage:
    >>> chart_by_names(('k1','k4'), parent)
    """
    indicator_types = []
    for name in names:
        indicator_types.append(models.IndicatorType.objects.filter(name__icontains=name)[0])
    x_ticks = []
    column = 0
    for child in parent.children:
        x_ticks.append(dict(v=column, label=child.name))
        column += 1
    x_ticks.append(dict(v=column, label=parent.name+' Average'))
    filename=''
    for name in names: filename+=name
    vertical_bar_chart("relatori/static/images/tmp/%s.png" % filename, indicators_by_parent_by_types(parent, indicator_types), x_ticks = x_ticks)


def chart_by_name_by_quarter(name, parent):
    """
    Given a of name (words) in IndicatorType names and an parent area
    Print stats per facility or sub-area
    return a list containing stats per facility per quarter to be consumed by pycha
    Usage: 
    >>> chart_by_name_by_quarter('k1', parent)
    """
    indicator_type = models.IndicatorType.objects.filter(name__icontains=name)[0]
    x_ticks = []
    column = 0
    for child in parent.children:
        x_ticks.append(dict(v=column, label=child.name))
        column += 1
    x_ticks.append(dict(v=column, label=parent.name+' Average'))
    vertical_bar_chart("relatori/static/images/tmp/%s.png" % name, indicators_by_parent_by_type_by_quarter(parent, indicator_type), x_ticks = x_ticks)
