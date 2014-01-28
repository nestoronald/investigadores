from django.db import models

class AreaInv(models.Model):
    # id_area = models.AutoField(primary_key=True)
    area = models.CharField("Area de Investigacion", max_length=80)


class SubareaInv(models.Model):
    id_sub_area = models.AutoField(primary_key=True)
    subarea = models.CharField("Subarea de Investigacion", max_length=80)
    area = models.ForeignKey(AreaInv)

class DisciplinaInv(models.Model):
    id_sub_area = models.AutoField(primary_key=True)
    disciplina_inv = models.CharField("Disciplina de Investigacion", max_length=80)
    subarea= models.ForeignKey(SubareaInv)

class Sexo(models.Model):
    sexo = models.CharField(max_length=30)
    def __unicode__(self):
        return self.sexo

class Investigador(models.Model):
    apellidos = models.CharField(max_length = 60)
    nombres = models.CharField(max_length = 30)
    resumen = models.TextField()
    web_personal = models.URLField("Web Personal",max_length = 80, blank=True)
    pais_nacimiento = models.CharField("Pais de Nacimiento", max_length = 50)
    sexo = models.ForeignKey(Sexo)
    email = models.EmailField(max_length = 75)
    dni = models.CharField(max_length = 50)
    fecha_nac = models.DateField("Fecha nacimiento")
    direccion_actual = models.CharField("Direccion Actual", max_length = 100, blank=True)
    telefono = models.CharField("telefono de Contacto", max_length = 20, blank=True)
    celular = models.CharField(max_length=15, blank=True)
    pais = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    distrito = models.CharField(max_length=30)
    Area_Investigacion = models.ManyToManyField(AreaInv)
    def __unicode__(self):
        nombrecompleto= "%s %s"%(self.nombres, self.apellidos)
        return nombrecompleto

# class Investigador_Area(models.Model):
#     id_area_inv = models.AutoField(primary_key=True)
#     id_area = models.ForeignKey(AreaInv)
#     id_inv = models.ForeignKey(Investigador)


class ExperienciaLaboral(models.Model):
    id_exp_lab = models.AutoField(primary_key=True)
    investigador = models.ForeignKey(Investigador)
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
    fx_ini = models.DateField('Fecha de Inicio')
    fx_fin = models.DateField('Fecha Fin')

class FormacionAcademica(models.Model):
    id_form_acad = models.AutoField(primary_key=True)
    investigador = models.ForeignKey(Investigador)
    grado = models.CharField("Grado Obtenido", max_length=100)
    nom_titulo = models.CharField("Nombre de Titulo", max_length=100)
    p_estudio = models.CharField("Pais de Estudio", max_length=60)
    c_estudios = models.CharField("Centro de Estudio", max_length=100)
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
    id_idioma = models.AutoField(primary_key=True)
    investigador = models.ForeignKey(Investigador)
    idioma = models.ForeignKey(Languaje)
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
    areaOCDE = models.ForeignKey(AreaOCDE)
    subareaOCDE = models.CharField(max_length=60)


# class AreaOCDE_SubareaOCDE(models.Model):
#     id_areasubarea = models.AutoField(primary_key=True)
#     id_areaocde = models.ForeignKey(AreaOCDE)
#     id_subareaocde = models.ForeignKey(SubareaOCDE)

class ProyectoInv(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    investigador = models.ForeignKey(Investigador)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    palabra_clave = models.CharField(max_length=50)
    fx_ini = models.DateField('Fecha de Inicio')
    fx_fin = models.DateField('Fecha Fin')
    rol = models.CharField(max_length=50)
    responsable = models.CharField(max_length=80)
    institucion_principal = models.CharField(max_length=120)
    institucion_colaboradora = models.CharField(max_length=120)
    monto = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    colaboradores = models.ManyToManyField(Colaboradores)
    subarea_OCDE = models.ManyToManyField(SubareaOCDE)


class ProduccionCientifica(models.Model):
    id_prodcien = models.AutoField(primary_key=True)
    investigador = models.ForeignKey(Investigador)
    tipo = models.CharField(max_length=60)
    rol = models.CharField(max_length=60)
    author_pri = models.CharField(max_length=60)
    coautores = models.CharField(max_length=60)
    id_colaboradores = models.ForeignKey(Colaboradores)
    titulo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=70)
    fx_produccion= models.DateField('Fecha de Produccion')
    palabra_clave = models.CharField(max_length=70)
    archivo = models.FileField(upload_to='.')

class Distinciones(models.Model):
    investigador = models.ForeignKey(Investigador)
    intitucion = models.CharField(max_length=75)
    nombre_dist = models.CharField(max_length=75)
    pais = models.CharField(max_length=60)
    web_referencia = models.CharField(max_length=85)
    fx_referencia = models.DateField('Fecha de Referencia')

# class ModelDemo(models.Model):
#     textorequerido = models.CharField(max_length=75)
#     textonorequerido = models.CharField(max_length=75, blank=True)
#     def __unicode__(self):
#         return self.textorequerido
class Student(models.Model):
    # FRESHMAN = 'FR'
    # SOPHOMORE = 'SO'
    # JUNIOR = 'JR'
    # SENIOR = 'SR'
    MEDIA_CHOICES = (
        ('Audio', (
                ('vinyl', 'Vinyl'),
                ('cd', 'CD'),
            )
        ),
        ('Video', (
                ('vhs', 'VHS Tape'),
                ('dvd', 'DVD'),
            )
        ),
        ('unknown', 'Unknown'),
    )
    year_in_school = models.CharField(max_length=4,choices=MEDIA_CHOICES)
class Demographic(models.Model):
    study_id = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Study ID', blank=True)
    date_enrolled = models.DateField(help_text='YYYY-MM-DD', null=True, verbose_name='Date subject signed consent', blank=True)
    file_upload = models.TextField(help_text='', null=True, verbose_name='file upload', blank=True) # This field type is a guess
    first_name = models.CharField(help_text='', null=True, max_length=2000, verbose_name='First Name', blank=True)
    last_name = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Last Name', blank=True)
    address = models.TextField(help_text='', null=True, verbose_name='Street, City, State, ZIP', blank=True) # This field type is a guess
    telephone_1 = models.CharField(help_text='Include Area Code', null=True, max_length=2000, verbose_name='Phone number', blank=True)
    telephone_2 = models.CharField(help_text='Include Area Code', null=True, max_length=2000, verbose_name='Second phone number', blank=True)
    sex = models.IntegerField(help_text='', null=True, verbose_name='Gender', blank=True, choices=[(0, 'Female'), (1, 'Male')]) # This field type is a guess
    email = models.EmailField(help_text='', null=True, verbose_name='E-mail', blank=True)
    num_children = models.IntegerField(help_text='', null=True, verbose_name='How many times has the subject given birth?', blank=True)
    given_birth = models.TextField(help_text='', null=True, verbose_name='Has the subject given birth before?', blank=True) # This field type is a guess
    ethnicity = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Ethnicity', choices=[(0, 'Hispanic or Latino'), (1, 'NOT Hispanic or Latino'), (2, 'Unknown / Not Reported')])
    race = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Race', choices=[(0, 'American Indian/Alaska Native'), (1, 'Asian'), (2, 'Native Hawaiian or Other Pacific Islander'), (3, 'Black or African American'), (4, 'White'), (5, 'More Than One Race'), (6, 'Unknown / Not Reported')])
    age = models.FloatField(help_text='', null=True, verbose_name='Age (years)', blank=True)
    dob = models.DateField(help_text='', null=True, verbose_name='Date of birth', blank=True)
    height = models.FloatField(help_text='', null=True, verbose_name='Height (cm)', blank=True)
    bmi = models.FloatField(help_text='', null=True, verbose_name='BMI', blank=True)
    weight = models.IntegerField(help_text='', null=True, verbose_name='Weight (kilograms)', blank=True)
    patient_document = models.TextField(help_text='', null=True, verbose_name='Patient document', blank=True) # This field type is a guess
    diabetes = models.IntegerField(help_text='', null=True, verbose_name='Patient has a diagnosis of diabetes mellitus?', blank=True, choices=[(0, 'No'), (1, 'Yes')]) # This field type is a guess
    comorbidities = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Any comorbid condition', blank=True)
    diabetes_type = models.IntegerField(help_text='', null=True, verbose_name='Type of Diabetes Mellitus', blank=True, choices=[(0, 'Type 1 insulin-dependent'), (1, 'Type 2 insulin-dependent'), (2, 'Type 2 non insulin-dependent')]) # This field type is a guess
    dialysis_initiation = models.DateField(help_text='', null=True, verbose_name='Date of first outpatient dialysis treatment', blank=True)
    access_type = models.IntegerField(help_text='', null=True, verbose_name='Type of vascular access', blank=True, choices=[(0, 'Graft'), (1, 'Fistula'), (2, 'Catheter with maturing graft'), (3, 'Catheter with maturing fistula')]) # This field type is a guess
    access_location = models.IntegerField(help_text='', null=True, verbose_name='Location of currently used vascular access', blank=True, choices=[(0, 'Forearm'), (1, 'Upper arm'), (2, 'Internal jugular vein'), (3, 'Subclavian vein'), (4, 'Other')]) # This field type is a guess
    dialysis_unit_name = models.CharField(help_text='', null=True, max_length=2000, verbose_name='Name of dialysis unit', blank=True)
    dialysis_unit_phone = models.CharField(help_text='Include Area Code', null=True, max_length=2000, verbose_name='Phone number', blank=True)
    dialysis_schedule_days = models.IntegerField(max_length=2000, blank=True, help_text='', null=True, verbose_name='Days of the week patient is dialyzed', choices=[(0, 'Monday-Wednesday-Friday'), (1, 'Tuesday-Thursday-Saturday'), (2, 'Other')])
    dialysis_schedule_time = models.IntegerField(help_text='', null=True, verbose_name='Shift patient is dialyzed', blank=True, choices=[(0, 'First shift'), (1, 'Second shift'), (2, 'Third shift'), (3, 'Fourth shift')]) # This field type is a guess
    subject_comments = models.TextField(help_text='', null=True, verbose_name='Comments', blank=True) # This field type is a guess
    etiology_esrd = models.IntegerField(help_text='', null=True, verbose_name='Etiology of ESRD', blank=True, choices=[(0, 'Diabetes'), (1, 'Hypertension'), (2, 'Glomerulonephritis'), (3, 'Polycystic Kidney Disease'), (4, 'Interstitial Nephritis'), (5, 'Hereditary Nephritis'), (6, 'Other')]) # This field type is a guess
    survey_1 = models.IntegerField(max_length=2000, blank=True, help_text='This describes the field', null=True, verbose_name='Test', choices=[(1, 'choice 1'), (2, 'choice 2')])
    checkbox_test_summary = models.CharField(help_text='0, option 1 | 1, option 2 | 2, option 3 | 3, option 4', null=True, max_length=2000, verbose_name='Checkbox', blank=True)


    class Meta:
         db_table = 'demographic'

