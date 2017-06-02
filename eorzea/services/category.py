from sqlalchemy import asc

from eorzea.models import CategoryModel


class CategoryService:
    @staticmethod
    def get_category_by_id(category_id):
        category = CategoryModel.query.get(category_id)
        return category

    @staticmethod
    def get_categories():
        categories = CategoryModel.query.filter_by(status=0).order_by(asc(CategoryModel.order)).all()
        return categories
