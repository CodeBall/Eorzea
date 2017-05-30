from eorzea.models import CategoryModel


class CategoryService:
    @staticmethod
    def get_category_by_id(category_id):
        category = CategoryModel.query.get(category_id)
        return category
