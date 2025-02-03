import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Question')),
                ('answer', ckeditor.fields.RichTextField(verbose_name='Answer')),
                ('question_hi', models.TextField(blank=True, verbose_name='Question (Hindi)')),
                ('question_bn', models.TextField(blank=True, verbose_name='Question (Bengali)')),
                ('answer_hi', ckeditor.fields.RichTextField(blank=True, verbose_name='Answer (Hindi)')),
                ('answer_bn', ckeditor.fields.RichTextField(blank=True, verbose_name='Answer (Bengali)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]