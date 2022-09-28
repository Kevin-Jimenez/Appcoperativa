import json
from re import template
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from .models import Cliente, Credito, Usuario
from django.http.response import JsonResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class ClienteViews(View):
    #method to resolve problem about cookies
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, doc=0):
        if(doc > 0):
            cli = list(Cliente.objects.filter(documento=doc).values())
            if (len(cli) > 0):
                clires = cli[0]
                datos={'CLIENTES => ':clires}
            else:
                datos={"Response: ": "Object not found.."}
        else:
            template_name="consultarcli.html"
            cli = Cliente.objects.all()
            #cli=list(Cliente.objects.values())
            datos={'cli':cli}
        #return JsonResponse (datos)   
        return render (request, template_name,datos) 

    def post(self, request):
        template_name = "adduser.html"
        Cliente.objects.create(documento=request.POST["documento"],
                                nombre = request.POST["nombre"], 
                                apellido = request.POST["apellido"],
                                correo = request.POST["correo"],
                                celular = request.POST["celular"])
        #data = json.loads(request.body)
        #Cliente.objects.create(documento=data['documento'], nombre = data['nombre'], apellido = data['apellido'],
        #correo = data['correo'], celular = data['celular'])
        #return JsonResponse(data)
        return redirect('/cliente/')

    def put(self, request, doc):
        data = json.loads(request.body)
        cli = list(Cliente.objects.filter(documento=doc).values())
        if(len(cli) > 0):
            clientes = Cliente.objects.get(documento = doc)
            clientes.nombre = data['nombre']
            clientes.apellido = data['apellido']
            clientes.correo = data['correo']
            clientes.celular = data['celular']
            clientes.save()
            message = {"Response: ": "Updated Successfully.."}
        else:
            message = {"Response: ": "Object not found.."}
        return JsonResponse(message)

    def delete(self, request, doc):
        cli = list(Cliente.objects.filter(documento = doc).values())
        if(len(cli) > 0):
            Cliente.objects.filter(documento = doc).delete()
            message = {"Response: ":"Deleted Successfully..."}
        else:
            message = {"Response: ": "Object not found.."}
        return JsonResponse(message)

class UsuarioViews(View):
    #method to resolve problem about cookies
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) 
    
    def get(self,request, id=0):
        if(id > 0):
            usu=list(Usuario.objects.filter(Document=id).values())
            if(len(usu) > 0):
                usuResponse=usu[0]
                data={"Message":usuResponse}
            else:
                data={"Message":"Data not Found"}
        else:
            usu=list(Usuario.objects.values())
            data={"Users: ":usu}
        return JsonResponse(data)

    def post(self,request):
        data = json.loads(request.body)
        cli = Cliente.objects.get(documento=data["documento"])
        Usuario.objects.create(Document=data["Document"],nameuser=data["nameuser"],password=data["password"],rol=data["rol"],documento=cli)

        return JsonResponse(data)

def loginUser(request):
    if(request.method=='POST'):
        try:
            validationUser = Usuario.objects.get(nameuser=request.POST['nameuser'],password=request.POST['password'])
            print(validationUser.Document)
            print(validationUser.rol)
            if (validationUser.rol=="Admin"):
                request.session['nameuser']=validationUser.nameuser
                request.session['Document']=validationUser.Document
                return render(request,'admin.html')
            elif (validationUser.rol=="Empleado"):
                request.session['nameuser']=validationUser.nameuser
                return render(request,'empleado.html')
            elif (validationUser.rol=="Cliente"):
                request.session['nameuser']=validationUser.nameuser
                return render(request,'cliente.html')
        except Usuario.DoesNotExist:
            message.success(request,"Usuario o Contraseña Incorrecto")
    return render(request, 'login.html')

def formRegister(request):
    return render(request,'adduser.html')

def formUpdate(request, doc):
    cliente = Cliente.objects.get(documento=doc)
    data={
        'cliente': cliente
    }

    return render(request, 'actualizaruser.html', data)

def updateCliente(request):
    documento=request.POST['documento']
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    correo=request.POST['correo']
    celular=request.POST['celular']
    cli=Cliente.objects.get(documento=documento)
    cli.nombre=nombre
    cli.apellido=apellido
    cli.correo=correo
    cli.celular=celular
    cli.save()
    return redirect('/cliente/')

def deleteCliente(request, doc):
    Cliente.objects.filter(documento = doc).delete()
    return redirect('/cliente/')

def exampleJoin(request, doc):
    data=Credito.objects.select_related('documento').filter(documento = doc)
    template_name="join.html"
    dat={"lista":data}
    return render(request,template_name,dat)






        
