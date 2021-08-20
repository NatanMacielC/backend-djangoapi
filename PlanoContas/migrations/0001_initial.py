# Generated by Django 3.2.6 on 2021-08-19 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanoContasReferencial',
            fields=[
                ('ID', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Codigo', models.CharField(max_length=50)),
                ('Descricao', models.CharField(max_length=150)),
                ('DataCadastro', models.DateTimeField(editable=False)),
                ('DataAlteracao', models.DateTimeField(null=True)),
                ('Ativo', models.BooleanField(default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmpresaPlanoContas',
            fields=[
                ('ID', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('EmpresaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresa')),
                ('PlanoContasReferencialID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlanoContas.planocontasreferencial')),
            ],
        ),
    ]