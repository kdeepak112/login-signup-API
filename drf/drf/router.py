from user_auth.viewsets import registerViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('registerUser',registerViewset)

