from django.urls import path
from .views import *
urlpatterns = [
     path('', homefn, name='home'),


    path('dashboard/', dashboardfn, name='dashboard'),

    path('tasks/', tasksfn, name='tasks'),

    path('todo/', todofn, name='todo'),

    path('calendar/', calendarfn, name='calendar'),

    # path('team/', teamfn, name='team'),

    path('reports/', reportsfn, name='reports'),

    path('notifications/', notificationsfn, name='notifications'),

    
    path('profile/', profilefn, name='profile'),
    path('add-task/', addtaskfn, name='addtask'),
    path('edit-task/<int:task_id>/', edittaskfn, name='edittask'),
    path('delete-task/<int:task_id>/', deletetaskfn, name='deletetask'),

]

