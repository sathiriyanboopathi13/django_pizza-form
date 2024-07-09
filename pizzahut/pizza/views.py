from django.shortcuts import render,HttpResponse
from .forms import PizzaForm,MultiplePizzaForm
from django .forms import formset_factory
from .models import Pizza

# Create your views here.
def homepage (request):
    return render(request,'pizza/home.html')
def order (request): # fbv = function based view
    multiple_pizza_form = MultiplePizzaForm() #empty form
    created_pizza_pk = None
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'your order for %s %s %s pizza was placed'%(filled_form.cleaned_data['topping1'],
                                                               filled_form.cleaned_data['topping2'],
                                                               filled_form.cleaned_data['size'])
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id # primary key
        else:
            note = 'somthing went wrong,please tryagain....'
        new_form = PizzaForm() # empty form
        return render(request, 'pizza/order.html', {'pizzaform':new_form ,'note':note,'multiple_pizza_form':multiple_pizza_form,'created_pizza_pk':created_pizza_pk})
    else:
        form = PizzaForm()  # empty from
        return render(request,'pizza/order.html',{'pizzaform':form,'multiple_pizza_form':multiple_pizza_form,'created_pizza_pk':created_pizza_pk})

def pizzas(request):
    number_of_pizzas= 2
    if request.method == 'GET':
        filled_form = MultiplePizzaForm(request.GET)
        if filled_form.is_valid():
            number_of_pizzas = filled_form.cleaned_data['number']
            print(number_of_pizzas)

    PizzasFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)  # formset class
    if request.method =='POST':
        filled_formset = PizzasFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
            note = 'your order Placed succesfully'
        else:
            note = 'sorry somthin went wrong'
        return HttpResponse('<h2>'+note+'</h2>') #<h2>'your order was placed'</h2>
        # return render(request,'pizza/pizzas.html',{'note':note})

    form_set = PizzasFormSet() #empty formset
    return render(request,'pizza/pizzas.html',{'form_set':form_set})

def edit(request,pk):
    pizza = Pizza.objects.get(pk=pk) #model obj
    filled_form = PizzaForm(instance=pizza) #form obj
    if request.method == 'POST':
        edited_form = PizzaForm(request.POST,instance=pizza)
        if edited_form.is_valid():
            edited_form.save()
            note = 'order was updated successfully'
        else:
            note = 'sorry please try again'
        return render(request,'pizza/edit.html',{'form':edited_form,'pk':pk,'note':note})
    return render(request,'pizza/edit.html',{'form':filled_form,'pk':pk})



