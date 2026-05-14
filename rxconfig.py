import reflex as rx

config = rx.Config(
    app_name="onepage_studio",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)