from django.db import models

class Investigador(models.Model):
    apellidos = models.CharField(max_length = 60)
    nombres = models.CharField(max_length = 30)
    resumen = models.TextField()
    web_personal = models.CharField(max_length = 80)
    pais_nacimiento = models.CharField(max_length = 50)
    pais_sexo = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    dni = models.CharField(max_length = 50)
    fecha_nac = models.DateTimeField('fecha nacimiento')
    nro_documento = models.CharField(max_length = 50)
    direccion_actual = models.CharField("Direccion Actual",max_length = 100)
    telefono = models.CharField("telefono de Contacto",max_length = 20)
    celular = models.CharField(max_length=15)
    pais = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    distrito = models.CharField(max_length=30)

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
    email_lab = models.CharField("Correo laboral",max_length=15)
    fx_ini = models.DateTimeField('Fecha de Inicio')
    fx_fin = models.DateTimeField('Fecha Fin')
    investigador = models.ForeignKey(Investigador)

class Formacion_Academica(models.Model):
    id_form_acad = models.AutoField(primary_key=True)
    grado = models.CharField("Grado Obtenido", max_length=20)
    nom_titulo = models.CharField("Nombre de Titulo", max_length=50)
    p_estudio = models.CharField("Pais de Estudio", max_length=15)
    fx_ini = models.DateTimeField('Fecha de Inicio')
    fx_fin = models.DateTimeField('Fecha Fin')
    investigador = models.ForeignKey(Investigador)

class Formacion_Continua(models.Model):
    id_form_cont = models.AutoField(primary_key=True)
    cap_continua = models.CharField("Capacitacion Continua", max_length=100)
    centro_estudios = models.CharField("Centro de Estudios", max_length=100)
    pais = models.CharField(max_length=30)
    frecuencia = models
















