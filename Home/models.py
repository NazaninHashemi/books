from django.db import models



# Create your models here.
class typeb(models.Model):
    onvan=models.CharField(max_length=80) 
    aks1=models.ImageField(upload_to = "Home/typeb",default="Home/image/cat6.jpg",null=True)
    def __str__(self):
        return self.onvan

class bookinfo(models.Model):
    namebook=models.CharField(max_length=80)
    aks1=models.ImageField(upload_to = "Home/typeb",default="Home/image/cat6.jpg",null=True)
    aks2=models.ImageField(upload_to = "Home/typeb",default="Home/image/cat6.jpg",null=True)
    nevisande=models.CharField(max_length=80)
    genre=models.CharField(max_length=80)
    kholase=models.TextField()
    def __str__(self):
        return self.namebook  
    
class tamas(models.Model):
    nam=models.CharField(max_length=80)
    email=models.CharField(max_length=80)
    phone=models.CharField(max_length=80)
    massage=models.TextField()
    def __str__(self):
        return self.email 
    


    
    
    
    
    
    
    
            