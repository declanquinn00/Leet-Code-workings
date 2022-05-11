import pygal
from pygal.style import Style
custom_style = Style(
  background='#e7d0f5',
  colors=('#ff1717', '#ff9c40', '#f7ff63', '#63ff6b', '#63d3ff'))

line_chart = pygal.Bar(style=custom_style)
line_chart.title = 'version-testing'
#line_chart.x_labels = map(str, range(1, 11))
line_chart.add('first_result', 554)
line_chart.add('final_result', 310)
line_chart.add('average_run', 302.9)
line_chart.add('P99', 554)
line_chart.add('P50', 267.5)
line_chart.render_to_file('version-testing.svg')
