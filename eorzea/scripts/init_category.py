from manage import app

from eorzea.extensions import db
from eorzea.models import CategoryModel


def init_category():
    categories = [
        {"slug": "book", "name": "图书", "order": "1", "description": "各种图书"},
        {"slug": "digital", "name": "数码", "order": "2", "description": "各种电子产品"},
        {"slug": "dress", "name": "服饰", "order": "3", "description": "外套,衬衫,裤子之类的衣服"},
        {"slug": "shoe&bag", "name": "鞋包", "order": "4", "description": "各种鞋子和包包"},
        {"slug": "ornament", "name": "配饰", "order": "5", "description": "衣服配饰,首饰等等"},
        {"slug": "cosmetic", "name": "个护", "order": "6", "description": "化妆品,护肤品,保健品神马的"},
    ]
    with app.app_context():
        for category in categories:
            ca = CategoryModel.query.filter_by(slug=category["slug"]).first()
            if ca is not None:
                continue

            ca = CategoryModel(
                slug=category["slug"],
                name=category["name"],
                order=category["order"],
                description=category["description"]
            )

            db.session.add(ca)

        db.session.commit()
