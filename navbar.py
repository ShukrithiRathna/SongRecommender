import dash_bootstrap_components as dbc
import dash_html_components as html

def Navbar():
    # navbar = dbc.NavbarSimple(
	# 	children=[
			
    #         dbc.NavItem(dbc.NavLink("Recommendations", href="/recommender")),
    #     ],
	# 	html.A(
    #             dbc.Row(
	# 		    [
    #          		dbc.Col(html.Img(src='assets/img/brand_img.png', height="30px"))
	# 			])
	# 		),
    #     brand="Music Recommendations",
    #       # brand=html.Img(src='assets/img/brand_img.png'),

    #     brand_href="/home",
    #     sticky="top",
    # )


    navbar = dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src='assets/img/brand_img.png', height="40px")),
                        dbc.Col(dbc.NavbarBrand("Music Recommendations", href="/home", className="ml-2 text-center")),
                    ],
                    # align="center",
                    # no_gutters=True,
                ),
                # href="https://plot.ly",
            ),
            dbc.NavItem(dbc.NavLink("Recommendations", href="/recommender"), style={'padding-left':'750px', 'color':'black'}),
        ],
		# brand_href="/home",
        sticky="top",
        # color="dark",
        # dark=True,
    )
    return navbar
