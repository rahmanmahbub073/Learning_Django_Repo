from django.shortcuts import render
from .models import Destination

# Create your views here.

# def index(request):
# return render(request, 'index.html', {'dest1':dest1})

# showing data without dbms
# def index(request):
#     dest1 = Destination()
#     dest1.Name = "Project Name1"
#     dest1.img = 'portfolio-1.jpg'
#     dest1.add = "123 Street, New York, USA"
#     dest1.offer = True

#     dest2 = Destination()
#     dest2.Name = "Project Name2"
#     dest2.img = 'portfolio-2.jpg'
#     dest2.add = "123 Street, New York, USA2"
#     dest2.offer = False

#     dest3 = Destination()
#     dest3.Name = "Project Name3"
#     dest3.img = 'portfolio-3.jpg'
#     dest3.add = "123 Street, New York, USA3"
#     dest3.offer = True

#     dest4 = Destination()
#     dest4.Name = "Project Name4"
#     dest4.img = 'portfolio-4.jpg'
#     dest4.add = "123 Street, New York, USA4"
#     dest4.offer = False

#     dest5 = Destination()
#     dest5.Name = "Project Name5"
#     dest5.img = 'portfolio-5.jpg'
#     dest5.add = "123 Street, New York, USA5"
#     dest5.offer = False

#     dest6 = Destination()
#     dest6.Name = "Project Name6"
#     dest6.img = 'portfolio-6.jpg'
#     dest6.add = "123 Street, New York, USA6"
#     dest6.offer = True

#     dests = [dest1, dest2, dest3, dest4, dest5, dest6]

#     return render(request, 'index.html', {'dests':dests})
 

# showing data from dbms
def index(request):
    dests=Destination.objects.all()
    return render(request, 'index.html', {'dests':dests})