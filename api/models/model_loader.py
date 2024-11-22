from . import orders, order_details, recipes, resources, sandwiches,payment, menu, menu_item

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    payment.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    menu_item.Base.metadata.create_all(engine)
