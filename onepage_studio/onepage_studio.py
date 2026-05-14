import reflex as rx

# ─────────────────────────────────────────
#  COLORES Y ESTILOS GLOBALES
# ─────────────────────────────────────────
BLUE = "#4472C4"
DARK_CARD = "#2b2b2b"
WHITE = "#ffffff"
GRAY_TEXT = "#666666"
BORDER = "#e0e0e0"

# Fuentes (agregar en rxconfig.py o aquí con stylesheets)
FONT_MONT = "Montserrat, sans-serif"
FONT_OPEN = "Open Sans, sans-serif"


# ─────────────────────────────────────────
#  NAVBAR
# ─────────────────────────────────────────
def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Logo
            rx.text(
                rx.text.span("1", font_weight="800"),
                rx.text.span("PAGE", font_weight="400"),
                font_family=FONT_MONT,
                font_size="22px",
                color=WHITE,
                letter_spacing="1px",
            ),
            rx.spacer(),
            # Links
            rx.hstack(
                *[
                    rx.link(
                        label,
                        href="#",
                        color=WHITE,
                        font_family=FONT_MONT,
                        font_size="12px",
                        font_weight="600",
                        letter_spacing="1px",
                        text_transform="uppercase",
                        text_decoration="none",
                        border_bottom=f"2px solid {WHITE}" if label == "HOME" else "2px solid transparent",
                        padding_bottom="4px",
                        _hover={"border_bottom": f"2px solid rgba(255,255,255,0.6)"},
                    )
                    for label in ["HOME", "ABOUT US", "OUR SERVICES", "OUR PORTFOLIO", "CONTACT US"]
                ],
                spacing="7",
            ),
            width="100%",
            align="center",
        ),
        background_color=BLUE,
        padding_x="40px",
        height="60px",
        width="100%",
    )


# ─────────────────────────────────────────
#  HERO
# ─────────────────────────────────────────
def hero() -> rx.Component:
    return rx.box(
        # Overlay
        rx.box(
            position="absolute",
            top="0", left="0", right="0", bottom="0",
            background="linear-gradient(rgba(60,90,160,0.72), rgba(60,90,160,0.72))",
            z_index="1",
        ),
        # Flecha izquierda
        rx.box(
            rx.icon("chevron-left", color=WHITE, size=18),
            position="absolute",
            left="20px",
            top="50%",
            transform="translateY(-50%)",
            z_index="10",
            background="rgba(255,255,255,0.25)",
            border_radius="50%",
            width="38px", height="38px",
            display="flex", align_items="center", justify_content="center",
            cursor="pointer",
            _hover={"background": "rgba(255,255,255,0.5)"},
        ),
        # Contenido central
        rx.vstack(
            rx.heading(
                "Game Development",
                font_family=FONT_MONT,
                font_size="42px",
                font_weight="800",
                color=WHITE,
                text_align="center",
            ),
            rx.text(
                "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
                color=WHITE,
                font_size="15px",
                font_style="italic",
                text_align="center",
                max_width="460px",
            ),
            rx.link(
                "GET STARTED",
                href="#",
                color=WHITE,
                border="2px solid white",
                padding="12px 36px",
                font_family=FONT_MONT,
                font_weight="700",
                font_size="13px",
                letter_spacing="2px",
                text_transform="uppercase",
                border_radius="2px",
                text_decoration="none",
                _hover={"background": WHITE, "color": BLUE},
            ),
            spacing="5",
            align="center",
            position="relative",
            z_index="2",
            padding_y="80px",
        ),
        # Flecha derecha
        rx.box(
            rx.icon("chevron-right", color=WHITE, size=18),
            position="absolute",
            right="20px",
            top="50%",
            transform="translateY(-50%)",
            z_index="10",
            background="rgba(255,255,255,0.25)",
            border_radius="50%",
            width="38px", height="38px",
            display="flex", align_items="center", justify_content="center",
            cursor="pointer",
            _hover={"background": "rgba(255,255,255,0.5)"},
        ),
        # Dots
        rx.hstack(
            rx.box(width="10px", height="10px", border_radius="50%", background=WHITE, cursor="pointer"),
            rx.box(width="10px", height="10px", border_radius="50%", background="rgba(255,255,255,0.5)", cursor="pointer"),
            rx.box(width="10px", height="10px", border_radius="50%", background="rgba(255,255,255,0.5)", cursor="pointer"),
            spacing="2",
            position="absolute",
            bottom="16px",
            left="50%",
            transform="translateX(-50%)",
            z_index="10",
        ),
        position="relative",
        width="100%",
        min_height="420px",
        background_image="url('https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=1200&q=80')",
        background_size="cover",
        background_position="center",
        display="flex",
        align_items="center",
        justify_content="center",
        overflow="hidden",
    )


# ─────────────────────────────────────────
#  HELPER: título de sección con línea
# ─────────────────────────────────────────
def section_title(text: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            text,
            font_family=FONT_MONT,
            font_size="26px",
            font_weight="700",
            color=BLUE,
        ),
        rx.box(width="50px", height="3px", background=BLUE),
        spacing="2",
        align="center",
    )


# ─────────────────────────────────────────
#  WELCOME
# ─────────────────────────────────────────
def welcome() -> rx.Component:
    return rx.vstack(
        section_title("Welcome To Our Website"),
        rx.text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec viverra at massa sit amet ultrices. "
            "Consequat mauris non interdum cursus, eros massa faucibus diam, in sodales quam ligula in est. Nullam "
            "ultrices turpis ut justo mollis tempus. Aliquam et tortor at quam laoreet condimentum ac nec leo. Lorem "
            "ipsum dolor sit amet, consectetur adipiscing elit. Donec mollis lacus tellus, eget fringilla enim feugiat in. "
            "Maecenas nec euismod lectus, nec congue eros. Nulla amet bibendum ut, fringilla sit amet est.",
            max_width="720px",
            text_align="center",
            font_size="13.5px",
            line_height="1.8",
            color=GRAY_TEXT,
        ),
        rx.button(
            "Read More",
            background="transparent",
            border=f"1px solid {BLUE}",
            color=BLUE,
            font_family=FONT_MONT,
            font_size="12px",
            font_weight="600",
            letter_spacing="1px",
            padding="9px 30px",
            border_radius="2px",
            cursor="pointer",
            _hover={"background": BLUE, "color": WHITE},
        ),
        spacing="5",
        align="center",
        padding_x="20px",
        padding_y="60px",
        width="100%",
        background=WHITE,
    )


# ─────────────────────────────────────────
#  MISSION STRIP
# ─────────────────────────────────────────
def mission_card(icon: str, title: str, bg: str) -> rx.Component:
    return rx.vstack(
        rx.icon(icon, color=WHITE, size=36),
        rx.heading(
            title,
            font_family=FONT_MONT,
            font_size="17px",
            font_weight="700",
            color=WHITE,
        ),
        rx.text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec viverra at massa sit amet ultrices. "
            "Nullam consequat, mauris non interdum cursus, eros massa faucibus diam, in sodales quam ligula in est.",
            font_size="12.5px",
            line_height="1.7",
            color="rgba(255,255,255,0.9)",
            text_align="center",
        ),
        spacing="3",
        align="center",
        background=bg,
        padding="40px 30px",
        flex="1",
    )


def mission_strip() -> rx.Component:
    return rx.hstack(
        mission_card("history", "Our Story", BLUE),
        mission_card("circle-dot", "Our Mission", DARK_CARD),
        mission_card("eye", "Our Vision", BLUE),
        spacing="0",
        width="100%",
        align="stretch",
    )


# ─────────────────────────────────────────
#  SERVICES
# ─────────────────────────────────────────
SERVICES = [
    ("monitor", "WEB DESIGN"),
    ("laptop-2", "WEB DEVELOPMENT"),
    ("settings", "THEME DEVELOPMENT"),
    ("gamepad-2", "GAME DEVELOPMENT"),
    ("smartphone", "APPS DEVELOPMENT"),
    ("tv-2", "DESKTOP APPLICATION"),
    ("layout-template", "WORDPRESS THEMES"),
    ("puzzle", "WORDPRESS PLUGINS"),
    ("headphones", "SUPPORT & IT"),
]


def service_item(icon: str, label: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.icon(icon, color=BLUE, size=18),
            border=f"2px solid {BLUE}",
            border_radius="50%",
            width="42px", height="42px",
            display="flex", align_items="center", justify_content="center",
            flex_shrink="0",
        ),
        rx.text(
            label,
            font_family=FONT_MONT,
            font_size="11.5px",
            font_weight="700",
            letter_spacing="0.8px",
            color="#333",
        ),
        spacing="3",
        border=f"1px solid {BORDER}",
        padding="16px 20px",
        border_radius="4px",
        cursor="pointer",
        _hover={"box_shadow": f"0 4px 16px rgba(68,114,196,0.15)", "border_color": BLUE},
        align="center",
    )


def services() -> rx.Component:
    return rx.vstack(
        section_title("Our Services"),
        rx.text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec viverra at massa sit amet ultrices.\nNullam consequat, mauris non interdum cursus.",
            color=GRAY_TEXT,
            font_size="13px",
            text_align="center",
            white_space="pre-line",
        ),
        rx.grid(
            *[service_item(icon, label) for icon, label in SERVICES],
            columns="3",
            spacing="4",
            width="100%",
            max_width="860px",
        ),
        spacing="5",
        align="center",
        padding_x="40px",
        padding_y="60px",
        width="100%",
        background=WHITE,
    )


# ─────────────────────────────────────────
#  STATS
# ─────────────────────────────────────────
STATS = [
    ("calendar", "12+", "YEARS OF EXPERIENCE"),
    ("check-circle", "999+", "COMPLETED PROJECTS"),
    ("users", "480+", "TOTAL CLIENTS"),
    ("heart", "15+", "AWARD WON"),
]


def stat_item(icon: str, number: str, label: str) -> rx.Component:
    return rx.vstack(
        rx.icon(icon, color=BLUE, size=34),
        rx.text(
            number,
            font_family=FONT_MONT,
            font_size="46px",
            font_weight="800",
            color="#222",
            line_height="1",
        ),
        rx.text(
            label,
            font_size="11px",
            letter_spacing="1.5px",
            text_transform="uppercase",
            color=GRAY_TEXT,
            font_weight="600",
        ),
        spacing="2",
        align="center",
        flex="1",
    )


def stats() -> rx.Component:
    return rx.hstack(
        *[stat_item(i, n, l) for i, n, l in STATS],
        spacing="0",
        width="100%",
        padding_x="40px",
        padding_y="50px",
        border_top=f"1px solid {BORDER}",
        border_bottom=f"1px solid {BORDER}",
        background=WHITE,
        justify="between",
    )


# ─────────────────────────────────────────
#  PORTFOLIO
# ─────────────────────────────────────────
PORTFOLIO_IMGS = [
    "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400&q=80",
    "https://images.unsplash.com/photo-1518770660439-4636190af475?w=400&q=80",
    "https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=400&q=80",
    "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=400&q=80",
    "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=400&q=80",
    "https://images.unsplash.com/photo-1523206489230-c012c64b2b48?w=400&q=80",
]

FILTERS = ["ALL", "WEB DEVELOPMENT", "GAME DEVELOPMENT", "APP DEVELOPMENT"]


def portfolio_item(src: str) -> rx.Component:
    return rx.box(
        rx.image(
            src=src,
            width="100%",
            height="100%",
            object_fit="cover",
            transition="transform 0.4s",
            _hover={"transform": "scale(1.07)"},
        ),
        overflow="hidden",
        aspect_ratio="4/3",
        border_radius="2px",
    )


def portfolio() -> rx.Component:
    return rx.vstack(
        section_title("Our Portfolio"),
        rx.text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec viverra at massa sit amet ultrices.\nNullam consequat, mauris non interdum cursus.",
            color=GRAY_TEXT,
            font_size="13px",
            text_align="center",
            white_space="pre-line",
        ),
        # Filtros
        rx.hstack(
            *[
                rx.text(
                    f,
                    font_family=FONT_MONT,
                    font_size="12px",
                    font_weight="700",
                    letter_spacing="1px",
                    color=BLUE if f == "ALL" else GRAY_TEXT,
                    border_bottom=f"2px solid {BLUE}" if f == "ALL" else "2px solid transparent",
                    padding_bottom="4px",
                    cursor="pointer",
                    _hover={"color": BLUE, "border_bottom": f"2px solid {BLUE}"},
                )
                for f in FILTERS
            ],
            spacing="6",
            border_bottom=f"1px solid {BORDER}",
            padding_bottom="12px",
        ),
        # Grid de imágenes
        rx.grid(
            *[portfolio_item(src) for src in PORTFOLIO_IMGS],
            columns="3",
            spacing="1",
            width="100%",
            max_width="860px",
        ),
        spacing="5",
        align="center",
        padding_x="40px",
        padding_y="60px",
        width="100%",
        background=WHITE,
    )


# ─────────────────────────────────────────
#  TESTIMONIAL
# ─────────────────────────────────────────
def testimonial() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="https://randomuser.me/api/portraits/men/32.jpg",
            width="72px",
            height="72px",
            border_radius="50%",
            object_fit="cover",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.text("Jayden Vaughan", font_family=FONT_MONT, font_weight="700", font_size="15px", color="#222"),
            rx.text("Science Technician", font_size="12px", color=BLUE),
            rx.text(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec viverra at massa sit amet ultrices. "
                "Nullam consequat, mauris non interdum cursus, eros massa faucibus diam, in sodales quam ligula in est.",
                font_size="13px",
                color=GRAY_TEXT,
                line_height="1.7",
            ),
            spacing="1",
            align="start",
        ),
        spacing="5",
        align="start",
        padding="40px",
        max_width="860px",
        width="100%",
        margin_x="auto",
        border_top=f"1px solid {BORDER}",
    )


# ─────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────
def footer() -> rx.Component:
    return rx.box(
        rx.text(
            "© 2024 1PAGE. All Rights Reserved.",
            color=WHITE,
            font_size="12.5px",
            letter_spacing="0.5px",
            text_align="center",
        ),
        background=BLUE,
        padding="18px",
        width="100%",
    )


# ─────────────────────────────────────────
#  PÁGINA PRINCIPAL
# ─────────────────────────────────────────
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        hero(),
        welcome(),
        mission_strip(),
        services(),
        stats(),
        portfolio(),
        testimonial(),
        footer(),
        spacing="0",
        width="100%",
        align="stretch",
        font_family=FONT_OPEN,
    )


# ─────────────────────────────────────────
#  APP
# ─────────────────────────────────────────
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Open+Sans:wght@400;600&display=swap",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css",
    ],
)
app.add_page(index, route="/")