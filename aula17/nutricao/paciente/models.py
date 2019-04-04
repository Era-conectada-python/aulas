from django.db import models


class Paciente(models.Model):
	nome = models.CharField(max_length=200)
	data_nascimento = models.DateField()
	telefone = models.CharField(max_length=15)
	profissao = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	sexo = models.CharField(max_length=20,
							blank=True,
							choices=[('1', 'masculino'),
									 ('2', 'feminino')])

	def __str__(self):
		return self.nome

class Dieta(models.Model):
	plano_alimentar = models.CharField(max_length=200)
	periodo = models.CharField(max_length=200,
							   choices=[('1', 'manhã'),
							     	    ('2', 'tarde'),
							     	    ('3', 'noite')])

	def __str__(self):
		return self.plano_alimentar

class Especialidade(models.Model):
	nome = models.CharField(max_length=200)
	descricao = models.TextField()

	def __str__(self):
		return self.nome

class Nutricionista(models.Model):
	nome = models.CharField(max_length=200)
	especialidades = models.ManyToManyField(Especialidade, related_name='nutricionistas')
	email = models.EmailField(max_length=254)
	telefone = models.CharField(max_length=15)
	crn = models.CharField(max_length=20)

	def __str__(self):
		return self.nome

class Avaliacao(models.Model):
	peso = models.DecimalField(max_digits=5, decimal_places=2)
	altura = models.DecimalField(max_digits=3, decimal_places=2)

class Consulta(models.Model):
	data_hora = models.DateTimeField()
	tipo = models.CharField(max_length=20,
							choices=[('1', 'consulta'),
									 ('2', 'retorno')])
	local = models.CharField(max_length=200)
	dieta = models.ForeignKey(Dieta, null=True, on_delete=models.CASCADE)
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	nutricionista = models.ForeignKey(Nutricionista, on_delete=models.CASCADE)
	avaliacao = models.OneToOneField(Avaliacao, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.tipo
