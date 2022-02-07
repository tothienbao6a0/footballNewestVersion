# Generated by Django 3.1.7 on 2022-01-02 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('correct_phrase', models.CharField(max_length=500)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='main.list')),
            ],
        ),
    ]