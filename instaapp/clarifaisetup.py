from clarifai.rest import ClarifaiApp
from instaapp.models import PostModel

def get_keywords():

    app = ClarifaiApp(api_key="d079c46cad9146699c7fa766b5904cb3")
    # clarifai api key = d079c46cad9146699c7fa766b5904cb3

    model = app.models.get("general-v1.3")
    response = model.predict_by_url(url=PostModel.image_url)
    return response