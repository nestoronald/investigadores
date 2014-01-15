from django.db import models

class AreaInv(models.Model):
    id_area = models.AutoField(primary_key=True)
    area = models.CharField("Area de Investigacion", max_length=80)


class SubareaInv(models.Model):
    id_sub_area = models.AutoField(primary_key=True)
    subarea = models.CharField("Subarea de Investigacion", max_length=80)
    area = models.ForeignKey(AreaInv)

class DisciplinaInv(models.Model):
    id_sub_area = models.AutoField(primary_key=True)
    disciplina_inv = models.CharField("Disciplina de Investigacion", max_length=80)
    subarea= models.ForeignKey(SubareaInv)

class Investigador(models.Model):
    apellidos = models.CharField(max_length = 60)
    nombres = models.CharField(max_length = 30)
    resumen = models.TextField()
    web_personal = models.CharField(max_length = 80)
    pais_nacimiento = models.CharField(max_length = 50)
    sexo = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 75)
    dni = models.CharField(max_length = 50)
    fecha_nac = models.DateTimeField('fecha nacimiento')
    direccion_actual = models.CharField("Direccion Actual",max_length = 100)
    telefono = models.CharField("telefono de Contacto",max_length = 20)
    celular = models.CharField(max_length=15)
    pais = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    distrito = models.CharField(max_length=30)

class Investigador_Area(models.Model):
    id_area_inv = models.AutoField(primary_key=True)
    id_area = models.ForeignKey(AreaInv)
    id_inv = models.ForeignKey(Investigador)


class ExperienciaLaboral(models.Model):
    id_exp_lab = models.AutoField(primary_key=True)
    nombre_ins = models.CharField("Nombre de la Institucion", max_length=80)
    direccion = models.CharField(max_length=80)
    cargo = models.CharField(max_length=50)
    descrip_cargo = models.CharField(max_length=120)
    sector = models.CharField(max_length=50)
    pais = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    distrito = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    pais = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    distrito = models.CharField(max_length=30)
    email_lab = models.EmailField("Correo laboral",max_length=75)
    fx_ini = models.DateTimeField('Fecha de Inicio')
    fx_fin = models.DateTimeField('Fecha Fin')
    investigador = models.ForeignKey(Investigador)

class FormacionAcademica(models.Model):
    id_form_acad = models.AutoField(primary_key=True)
    grado = models.CharField("Grado Obtenido", max_length=20)
    nom_titulo = models.CharField("Nombre de Titulo", max_length=50)
    p_estudio = models.CharField("Pais de Estudio", max_length=15)
    fx_ini = models.DateTimeField('Fecha de Inicio')
    fx_fin = models.DateTimeField('Fecha Fin')
    investigador = models.ForeignKey(Investigador)

class FormacionContinua(models.Model):
    id_form_cont = models.AutoField(primary_key=True)
    cap_continua = models.CharField("Capacitacion Continua", max_length=100)
    cent_est = models.CharField("Centro de Estudios", max_length=100)
    pais = models.CharField(max_length=30)
    frecuencia = models.CharField(max_length=30)
    cant_frec = models.CharField("Cantidad de frecuencia", max_length=10)
    fx_ini = models.DateTimeField('Fecha de Inicio')
    fx_fin = models.DateTimeField('Fecha Fin')
    investigador = models.ForeignKey(Investigador)

class Idioma(models.Model):
    id_idioma = models.AutoField(primary_key=True)
    des_idioma = models.CharField("Descripcion de Idioma", max_length=60)
    lectura = models.CharField(max_length=60)
    conversacion = models.CharField(max_length=60)
    escritura = models.CharField(max_length=60)
    forma_apren = models.CharField("Forma de Aprendizaje", max_length=60)

class Colaboradores(models.Model):
    id_colaboradores = models.AutoField(primary_key=True)
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=60)
    email = models.EmailField(max_length=75)

class AreaOCDE(models.Model):
    id_areaocde = models.AutoField(primary_key=True)
    AreaOCDE = models.CharField(max_length=60)

class SubareaOCDE(models.Model):
    id_subareaocde = models.AutoField(primary_key=True)
    SubareaOCDE = models.CharField(max_length=60)

class AreaOCDE_SubareaACDE(models.Model):
    id_areasubarea = models.AutoField(primary_key=True)
    id_areaocde = models.ForeignKey(AreaOCDE)
    id_subareaocde = models.ForeignKey(SubareaOCDE)

class ProyectoInv(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    palabra_clave = models.CharField(max_length=50)
    fx_ini = models.DateTimeField('Fecha de Inicio')
    fx_fin = models.DateTimeField('Fecha Fin')
    rol = models.CharField(max_length=50)
    responsable = models.CharField(max_length=80)
    institucion_principal = models.CharField(max_length=120)
    institucion_colaboradora = models.CharField(max_length=120)
    monto = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    id_colaboradores = models.ForeignKey(Colaboradores)
    id_areasubarea = models.ForeignKey(AreaOCDE_SubareaACDE)

class ProduccionCientifica(models.Model):
    id_prodcien = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=60)
    rol = models.CharField(max_length=60)
    author_pri = models.CharField(max_length=60)
    coautores = models.CharField(max_length=60)
    id_colaboradores = models.ForeignKey(Colaboradores)
    titulo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=70)
    fx_produccion= models.DateTimeField('Fecha de Produccion')
    palabra_clave = models.CharField(max_length=70)
    archivo = models.FileField(upload_to='.')

class Distinciones(models.Model):
    intitucion = models.CharField(max_length=75)
    nombre_dist = models.CharField(max_length=75)
    pais = models.CharField(max_length=60)
    web_referencia = models.CharField(max_length=85)
    fx_referencia = models.DateTimeField('Fecha de Referencia')