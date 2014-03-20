import datetime
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from base import Base, db_session
from date import format_date

class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True)
    eng_name = Column(String(64), nullable=False)
    chin_name = Column(String(64), nullable=False)
    pinyin = Column(String(64), nullable=True)
    desc = Column(String(64), nullable=True)

    @staticmethod
    def get_dish_by_id(id):
        dish = db_session.query(Dish).get(id)
        return dish

    @staticmethod
    def jsonify(dish):
        data = {
            'dish': {
                'id': dish.id,
                'chin_name': dish.chin_name,
                'eng_name': dish.eng_name,
            }
        }
        if dish.reviews:
            reviews = [{'username': review.user.username, 'date': format_date(review.date), 'text': review.text} for review in dish.reviews]
            data['dish']['reviews'] = reviews

        if dish.dish_tags:
            tags = [dish_tag.tag.name for dish_tag in dish.dish_tags]
            data['dish']['tags'] = tags

        return data

    @staticmethod
    def find_match(word):
        #TODO
        return None

    @staticmethod
    def find_similar(word):
        #TODO
        return []