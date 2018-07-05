import dash_html_components as html
import dash_core_components as dcc

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='http://logonoid.com/images/vanguard-logo.png', height='40', width='160')
        ], className="ten columns padded"),

        html.Div([
            dcc.Link('Full View   ', href='/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Vanguard 500 Index Fund Investor Shares')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Overview   ', href='/overview', className="tab first"),

        dcc.Link('Price Performance   ', href='/price-performance', className="tab"),

        dcc.Link('Portfolio & Management   ', href='/portfolio-management', className="tab"),

        dcc.Link('Fees & Minimums   ', href='/fees', className="tab"),

        dcc.Link('Distributions   ', href='/distributions', className="tab"),

        dcc.Link('News & Reviews   ', href='/news-and-reviews', className="tab")

    ], className="row ")
    return menu
