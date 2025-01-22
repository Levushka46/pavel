from django.urls import path
from .views import SubmitDataView, PerevalDetailView, PerevalUpdateView, PerevalListView

urlpatterns = [
    path('submitData/', SubmitDataView.as_view(), name='submit-data'),
    path('submitData/<int:pk>/', PerevalDetailView.as_view(), name='pereval-detail'),
    path('submitData/<int:pk>/update/', PerevalUpdateView.as_view(), name='pereval-update'),
    path('submitData/list/', PerevalListView.as_view(), name='pereval-list'),
]