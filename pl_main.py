"""
Icon https://icon-sets.iconify.design/?category=Animated+Icons

"""


import dash
from dash import Dash, html, Input, Output, State, callback, _dash_renderer
import dash_mantine_components as dmc
#from jupyter_dash import JupyterDash
from dash_iconify import DashIconify

_dash_renderer._set_react_version("18.2.0")

app = Dash(external_stylesheets=dmc.styles.ALL)

display = dmc.Tabs(
    [
        dmc.Tooltip(
            dmc.Avatar("PW", color="cyan", radius="xl"),
            label="何碧薇医师",
            position="top"
        ),
        dmc.TabsList(
            [
                dmc.TabsTab("Dashboard 首页", leftSection=DashIconify(icon="mage:dashboard-chart-notification"), value="dashboard"),
                dmc.TabsTab("Herbs 药材", leftSection=DashIconify(icon="icon-park:traditional-chinese-medicine"), value="herbs"), # Under herbs have unit price
                dmc.TabsTab("Patients 患者", leftSection=DashIconify(icon="fluent:patient-20-regular"), value="patients"), # List of patients, link to patient history
                dmc.TabsTab("Products 产品", leftSection=DashIconify(icon="ic:baseline-production-quantity-limits"), value="products"), # Under products have unit price

                dmc.TabsTab("Search 搜索", leftSection=DashIconify(icon="ant-design:file-search-outlined"), value="search"),  # Search by Name, IC, herbs, product and etc
                dmc.TabsTab("Settings 设置", leftSection=DashIconify(icon="tabler:settings"), value="settings"), # Edit patient info, herb price, product
            ]
        ),
         dmc.TabsPanel("Dashboard tab content", value="dashboard"),
         dmc.TabsPanel("Herbs tab content", value="herbs"),
         dmc.TabsPanel("Patients tab content", value="patients"),
         dmc.TabsPanel("Products tab content", value="products"),
         dmc.TabsPanel("Search tab content", value="search"),
         dmc.TabsPanel("Settings tab content", value="settings"),
    ],
    #color="red",
    orientation="vertical",
)

display2 = html.Div([
    display

])
# display3 = dmc.Group(
#     children=[
#         dmc.Avatar(
#             src="https://avatars.githubusercontent.com/u/91216500?v=4", radius="xl"
#         ),
#         dmc.Avatar(
#             src="ollama_logo.png", radius="x1"
#         ),
#         # default placeholder
#         dmc.Avatar(radius="xl"),
#         # initials
#         dmc.Avatar("MK", color="cyan", radius="xl"),
#         # icon
#         dmc.Avatar(DashIconify(icon="radix-icons:star"), color="blue", radius="xl"),
#     ],
# )

maindisplay = dmc.AppShell(
    [
        dmc.AppShellHeader("Header", px=25),
        #dmc.AppShellNavbar(display),
        #dmc.AppShellAside("Aside", withBorder=False),
        dmc.AppShellMain(children=[display2]), # Content is here
        dmc.AppShellFooter("Footer"),
    ],
    header={"height": 70},
    padding="xl",
    zIndex=1400,
    # navbar={
    #     "width": 150,
    #     "breakpoint": "sm",
    #     "collapsed": {"mobile": True},
    # },
    footer={"height":20},
    # aside={
    #     "width": 300,
    #     "breakpoint": "xl",
    #     "collapsed": {"desktop": False, "mobile": True},
    # },
)

app.layout = dmc.MantineProvider(maindisplay)


if __name__ == "__main__":
    app.run(debug=True)
