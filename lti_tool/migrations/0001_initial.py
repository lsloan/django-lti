# Generated by Django 3.2.9 on 2021-12-13 21:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_key', models.TextField(verbose_name='public key')),
                ('private_key', models.TextField(verbose_name='private key')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'verbose_name': 'JWK',
                'verbose_name_plural': 'JWKs',
                'get_latest_by': 'datetime_created',
            },
        ),
        migrations.CreateModel(
            name='LtiDeployment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deployment_id', models.CharField(max_length=255, verbose_name='deployment ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'verbose_name': 'LTI deployment',
                'verbose_name_plural': 'LTI deployments',
            },
        ),
        migrations.CreateModel(
            name='LtiRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('uuid', models.UUIDField(default=uuid.uuid4, verbose_name='UUID')),
                ('issuer', models.CharField(max_length=255, verbose_name='issuer')),
                ('client_id', models.CharField(max_length=255, verbose_name='client ID')),
                ('auth_url', models.URLField(verbose_name='auth URL')),
                ('token_url', models.URLField(verbose_name='access token URL')),
                ('keyset_url', models.URLField(verbose_name='keyset URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('public_key', models.TextField(blank=True, verbose_name='public key')),
                ('private_key', models.TextField(blank=True, verbose_name='private key')),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'verbose_name': 'LTI registration',
                'verbose_name_plural': 'LTI registrations',
            },
        ),
        migrations.AddConstraint(
            model_name='ltiregistration',
            constraint=models.UniqueConstraint(fields=('issuer', 'client_id'), name='unique_client_id_per_issuer'),
        ),
        migrations.AddField(
            model_name='ltideployment',
            name='registration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deployments', to='lti_tool.ltiregistration', verbose_name='registration'),
        ),
        migrations.AddConstraint(
            model_name='ltideployment',
            constraint=models.UniqueConstraint(fields=('registration', 'deployment_id'), name='unique_deployment_id_per_registration'),
        ),
    ]