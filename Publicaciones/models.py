# -*- encoding: utf-8 -*-
from django.db import models

class AreaInv(models.Model):
    # id_area = models.AutoField(primary_key=True)
    area = models.CharField("Area de Investigacion", max_length=80)
    def __unicode__(self):
        return self.area

class Investigador(models.Model):
    apellidos = models.CharField(max_length = 60)
    nombres = models.CharField(max_length = 30)
    resumen = models.TextField()
    web_personal = models.URLField("Web Personal",max_length = 80, blank=True)
    pais_nacimiento = models.CharField("Pais de Nacimiento", max_length = 50)
    sex = models.IntegerField(null=True, verbose_name='Sexo', blank=True, choices=[(0, 'Femenino'), (1, 'Masculino')])
    email = models.EmailField(max_length = 75)
    dni = models.CharField(max_length = 50)
    fecha_nac = models.DateField('Fecha de Nacimiento')
    dir_actual = models.CharField("Dirección actual", max_length = 100, blank=True)
    telefono = models.CharField("Telefono de contacto", max_length = 20, blank=True)
    celular = models.CharField(max_length=15, blank=True)
    pais = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    distrito = models.CharField(max_length=30)
    area_inv = models.ManyToManyField(AreaInv,verbose_name='Area de Investigación')
    subarea_inv = models.CharField(max_length=80, verbose_name='Subarea de Investigación')
    disciplina = models.CharField(max_length=80, verbose_name='Disciplina de Investigación')
    def __unicode__(self):
        nombrecompleto = "%s %s"%(self.nombres, self.apellidos)
        return nombrecompleto


class ExperienciaLaboral(models.Model):
    id_exp_lab = models.AutoField(primary_key=True)
    investigador = models.ForeignKey(Investigador)
    nombre_ins = models.CharField("Nombre de la Institucion", max_length=80)
    direccion = models.CharField(max_length=80)
    cargo = models.CharField(max_length=50)
    descrip_cargo = models.TextField("Descripción de cargo:",max_length=120)
    sector = models.IntegerField(blank=True,choices=[(0, 'Publico'), (1, 'Privado')])
    pais = models.CharField(max_length=70, blank=True)
    region = models.CharField(max_length=70, blank=True)
    provincia = models.CharField(max_length=70, blank=True)
    distrito = models.CharField(max_length=70, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    email_lab = models.EmailField("Correo laboral",max_length=75, blank=True)
    fx_ini = models.DateField('Fecha de Inicio')
    fx_fin = models.DateField('Fecha Fin')
    def __unicode__(self):
        completo = "%s %s %s"%(self.investigador.nombres, self.investigador.apellidos, self.cargo)
        return completo

class FormacionAcademica(models.Model):
    id_form_acad = models.AutoField(primary_key=True)
    investigador = models.ForeignKey(Investigador)
    grado = models.IntegerField(verbose_name="Grado Obtenido",choices=[(0, 'Bachiller'), (1, 'Maestria'),(2,'Doctorado'),(3,'Ph.D')])
    nom_titulo = models.TextField(verbose_name="Nombre de Titulo", max_length=200)
    p_estudio = models.CharField("Pais de Estudio", max_length=80)
    c_estudios = models.TextField(verbose_name="Centro de Estudio")
    fx_ini = models.DateField('Fecha de Inicio')
    fx_fin = models.DateField('Fecha Fin')
    def __unicode__(self):
        nombrecompleto= "%s %s %s"%(self.investigador.nombres, self.investigador.apellidos, self.nom_titulo)
        return nombrecompleto


class FormacionContinua(models.Model):
    id_form_cont = models.AutoField(primary_key=True)
    investigador = models.ForeignKey(Investigador)
    cap_continua = models.CharField("Capacitacion Continua", max_length=100)
    cent_est = models.CharField("Centro de Estudios", max_length=100)
    pais = models.CharField(max_length=30)
    frecuencia = models.CharField(max_length=30)
    cant_frec = models.CharField("Cantidad de frecuencia", max_length=10)
    fx_ini = models.DateField('Fecha de Inicio')
    fx_fin = models.DateField('Fecha Fin')


class Languaje(models.Model):
    iddioma = models.CharField("Idioma", max_length=60)
    def __unicode__(self):
        return self.iddioma

class Idioma(models.Model):
    investigador = models.ForeignKey(Investigador)
    idioma = models.ForeignKey(Languaje)
    lectura = models.IntegerField(choices=[(0, 'Básico'), (1, 'Intermedio'),(2,'Avanzado')])
    conversacion = models.IntegerField(choices=[(0, 'Básico'), (1, 'Intermedio'),(2,'Avanzado')])
    escritura = models.IntegerField(choices=[(0, 'Básico'), (1, 'Intermedio'),(2,'Avanzado')])
    forma_apren = models.CharField("Forma de Aprendizaje", max_length=200, blank=True)
    len_mat = models.IntegerField(help_text="Indique si el idioma que está registrando es su lengua materna",verbose_name="Lengua Materna", choices=[(0, 'Si'), (1, 'No')])
    def __unicode__(self):
        nombrecompleto= "%s %s %s"%(self.investigador.nombres, self.investigador.apellidos, self.idioma.iddioma)
        return nombrecompleto

class Colaboradores(models.Model):
    id_colaboradores = models.AutoField(primary_key=True)
    apellidos = models.CharField(max_length=150)
    nombres = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    def __unicode__(self):
        return "%s %s"%(self.apellidos,self.nombres)

class Coautores(models.Model):
    apellidos = models.CharField(max_length=150)
    nombres = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    def __unicode__(self):
        return "%s %s"%(self.apellidos,self.nombres)

class AreaOCDE(models.Model):
    id_areaocde = models.AutoField(primary_key=True)
    AreaOCDE = models.CharField(max_length=60)

# class SubareaOCDE(models.Model):
#     id_subareaocde = models.AutoField(primary_key=True)
#     areaOCDE = models.ForeignKey(AreaOCDE)
#     subareaOCDE = models.CharField(max_length=60)


# class AreaOCDE_SubareaOCDE(models.Model):
#     id_areasubarea = models.AutoField(primary_key=True)
#     id_areaocde = models.ForeignKey(AreaOCDE)
#     id_subareaocde = models.ForeignKey(SubareaOCDE)

class ProyectoInv(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    investigador = models.ForeignKey(Investigador)
    titulo = models.TextField()
    descripcion = models.TextField()
    palabra_clave = models.CharField(max_length=50,blank=True)
    fx_ini = models.DateField('Fecha de Inicio')
    fx_fin = models.DateField('Fecha Fin')
    rol = models.CharField(max_length=50,blank=True)
    responsable = models.CharField(max_length=80)
    institucion_principal = models.CharField(max_length=120,blank=True)
    institucion_colaboradora = models.CharField(max_length=120,blank=True)
    monto = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    colaboradores = models.ManyToManyField(Colaboradores,blank=True)
    area_OCDE = models.ManyToManyField(AreaOCDE, verbose_name='Area OCDE',blank=True)
    subarea_OCDE = models.CharField(verbose_name='Subarea OCDE',max_length=50,blank=True)
    def __unicode__(self):
        completo = "%s %s %s"%(self.titulo,self.investigador.nombres,self.investigador.apellidos)
        return completo

class ProduccionCientifica(models.Model):
    id_prodcien = models.AutoField(primary_key=True)
    investigador = models.ForeignKey(Investigador)
    tipo = models.CharField(max_length=60)
    rol = models.CharField(max_length=60, blank=True)
    author_pri = models.CharField(max_length=60, blank=True)
    coautores = models.ManyToManyField(Coautores,blank=True)
    colaboradores = models.ManyToManyField(Colaboradores,blank=True)
    titulo = models.TextField()
    ubicacion = models.TextField(blank=True)
    fx_produccion= models.DateField('Fecha de Produccion')
    meta_tag = models.TextField(verbose_name='Palabras clave',blank=True)
    archivo = models.FileField(upload_to='.',blank=True)
    def __unicode__(self):
        completo = "%s %s %s"%(self.titulo,self.investigador.nombres,self.investigador.apellidos)
        return completo

class Distinciones(models.Model):
    investigador = models.ForeignKey(Investigador)
    intitucion = models.CharField(max_length=75)
    nombre_dist = models.TextField(verbose_name='Nombre de Distinción')
    pais = models.CharField(max_length=60)
    web_referencia = models.CharField(max_length=85)
    fx_referencia = models.DateField('Fecha de Referencia')
    def __unicode__(self):
        completo = "%s %s %s"%(self.nombre_dist,self.investigador.nombres,self.investigador.apellidos)
        return completo
