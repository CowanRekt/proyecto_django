from django.shortcuts import render

MI_PERFIL = {
    'mi_nombre': 'Zambrano Valdiviezo '
                 'Harold Adrián',
    'profesion': 'Ingeniero en Sotfware ',
    'email': 'haroldadrian2000@gmail.com',
    'github': 'https://github.com/CowanRekt',

}

def portada(request):
    return render(request, 'core/index.html', MI_PERFIL)

def about(request):
    context = {
        **MI_PERFIL,
        'biografia': 'Nací el 12 de Febrero del año 2000 en Ecuador-Manabí-Portoviejo. Soy estudiante de la carrera de Ingeniería en Software en la Universidad Técnica de Manabí. Me gusta mucho el tema tecnológico y la programación, razón por la cual estudio esta carrera. Mi meta es ser un profesional de renombre y trabajar con grandes empresas o ser mi propio jefe.',
        'biografia_extra': '',
    }
    return render(request, 'core/about.html', context)

def contact(request):
    context = {
        **MI_PERFIL,
        'descripcion_contacto': "Apasionado por la tecnología y disponible para nuevos retos profesionales y proyectos innovadores.",
        'telefono': '+593 93 938 4464',
        'honorarios': '20$/h',
    }
    return render(request, 'core/contact.html', context)