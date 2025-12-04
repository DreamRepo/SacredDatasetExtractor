import dash
import dash_bootstrap_components as dbc


def create_app() -> tuple[dash.Dash, "dash.Dash.server"]:
    """
    Create and return a Dash app instance and its underlying Flask server.
    """
    app = dash.Dash(
        __name__,
        external_stylesheets=[
            dbc.themes.LUX,
            dbc.icons.BOOTSTRAP,
            "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css",
        ],
    )
    return app, app.server


