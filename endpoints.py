from flask_restful import Resource
from .dalle_api_call import create_images


class GenerateImages(Resource):
    def get(self, prompt):
        return create_images(prompt)
