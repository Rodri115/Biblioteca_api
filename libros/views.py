from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Libro, Autor, Genero, Calificacion
from .forms import LibroForm, AutorForm, GeneroForm, CalificacionForm
from django.core.paginator import Paginator


def es_admin(user):
    return user.is_superuser

# ---- CRUD LIBRO ----
@login_required
@user_passes_test(es_admin)
def libro_list(request):
    libros = Libro.objects.all()
    paginator = Paginator(libros, 10)  # 10 libros por página
    page = request.GET.get('page')
    libros_paginados = paginator.get_page(page)
    return render(request, 'libros/libro_list.html', {'libros': libros_paginados})


@login_required
@user_passes_test(es_admin)
def libro_create(request):
    form = LibroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Libro creado correctamente.")
        return redirect('libro_list')
    return render(request, 'libros/libro_form.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def libro_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    form = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if form.is_valid():
        form.save()
        messages.success(request, "Libro actualizado correctamente.")
        return redirect('libro_list')
    return render(request, 'libros/libro_form.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def libro_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, "Libro eliminado correctamente.")
        return redirect('libro_list')
    return render(request, 'libros/confirm_delete.html', {'obj': libro, 'tipo': 'libro'})

# ---- CRUD AUTOR ----
@login_required
@user_passes_test(es_admin)
def autor_list(request):
    autores = Autor.objects.all()
    paginator = Paginator(autores, 10)
    page = request.GET.get('page')
    autores_paginados = paginator.get_page(page)
    return render(request, 'libros/autor_list.html', {'autores': autores_paginados})


@login_required
@user_passes_test(es_admin)
def autor_create(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Autor creado correctamente.")
        return redirect('autor_list')
    return render(request, 'libros/autor_form.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        messages.success(request, "Autor actualizado correctamente.")
        return redirect('autor_list')
    return render(request, 'libros/autor_form.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, "Autor eliminado correctamente.")
        return redirect('autor_list')
    return render(request, 'libros/confirm_delete.html', {'obj': autor, 'tipo': 'autor'})

# ---- CRUD GÉNERO ----
@login_required
@user_passes_test(es_admin)
def genero_list(request):
    generos = Genero.objects.all()
    paginator = Paginator(generos, 10)
    page = request.GET.get('page')
    generos_paginados = paginator.get_page(page)
    return render(request, 'libros/genero_list.html', {'generos': generos_paginados})


@login_required
@user_passes_test(es_admin)
def genero_create(request):
    form = GeneroForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Género creado correctamente.")
        return redirect('genero_list')
    return render(request, 'libros/genero_form.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def genero_update(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    form = GeneroForm(request.POST or None, instance=genero)
    if form.is_valid():
        form.save()
        messages.success(request, "Género actualizado correctamente.")
        return redirect('genero_list')
    return render(request, 'libros/genero_form.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def genero_delete(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        genero.delete()
        messages.success(request, "Género eliminado correctamente.")
        return redirect('genero_list')
    return render(request, 'libros/confirm_delete.html', {'obj': genero, 'tipo': 'género'})

# ---- CRUD CALIFICACIÓN ----
@login_required
@user_passes_test(es_admin)
def calificacion_list(request):
    calificaciones = Calificacion.objects.all()
    paginator = Paginator(calificaciones, 10)
    page = request.GET.get('page')
    calificaciones_paginadas = paginator.get_page(page)
    return render(request, 'libros/calificacion_list.html', {'calificaciones': calificaciones_paginadas})


@login_required
@user_passes_test(es_admin)
def calificacion_create(request):
    form = CalificacionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Calificación creada correctamente.")
        return redirect('calificacion_list')
    return render(request, 'libros/calificacion_form.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def calificacion_update(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    form = CalificacionForm(request.POST or None, instance=calificacion)
    if form.is_valid():
        form.save()
        messages.success(request, "Calificación actualizada correctamente.")
        return redirect('calificacion_list')
    return render(request, 'libros/calificacion_form.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def calificacion_delete(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        calificacion.delete()
        messages.success(request, "Calificación eliminada correctamente.")
        return redirect('calificacion_list')
    return render(request, 'libros/confirm_delete.html', {'obj': calificacion, 'tipo': 'calificación'})
