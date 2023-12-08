from django.shortcuts import render, redirect
from .forms import ReservaForm

def hacer_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            return redirect('pagina_exitosa')
    else:
        form = ReservaForm()
    
    return render(request, 'reservas/hacer_reserva.html', {'form': form})