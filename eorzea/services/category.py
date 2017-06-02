from sqlalchemy import asc

from eorzea.models import CategoryModel
from eorzea.extensions import db


class CategoryService:
    @staticmethod
    def get_category_by_id(category_id):
        category = CategoryModel.query.get(category_id)
        return category

    @staticmethod
    def get_category_by_slug(slug):
        category = CategoryModel.query.filter_by(slug=slug).first()
        return category

    @staticmethod
    def get_categories():
        categories = CategoryModel.query.filter_by(status=0).order_by(asc(CategoryModel.order)).all()
        return categories

    @staticmethod
    def get_category_choices():
        return db.session.query(CategoryModel.slug, CategoryModel.name).filter_by(status=0).all()
