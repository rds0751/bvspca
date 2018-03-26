from django.conf import settings
from django.core.mail import EmailMessage
from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel
from wagtail.core.fields import StreamField
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


class MenuTitleable(models.Model):
    menu_title = models.CharField(verbose_name='menu title', max_length=100, blank=True)

    class Meta:
        abstract = True


class Attachable(models.Model):
    attachments = StreamField([
        ('document', DocumentChooserBlock(icon='fa-file-text')),
    ], blank=True,)

    class Meta:
        abstract = True


class MetaTagable(models.Model):
    def seo_and_social_meta_values(self):
        site_short_name = getattr(settings, 'SPCA_SITE_SHORT_NAME')
        title = self.seo_title if self.seo_title else self.title
        return {
            'title': '{} | {}'.format(title, site_short_name),
            'description': self.search_description,
        }

    class Meta:
        abstract = True


class PageDesignMixin(models.Model):
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='page banner image',
        help_text='This image should be exactly 1600px wide and 560px high.'
    )
    menu_item_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='menu image',
    )

    content_panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel('banner_image'),
                ImageChooserPanel('menu_item_image'),
            ],
            heading='Page Design Elements',
            classname='collapsible collapsed',
        ),
    ]

    class Meta:
        abstract = True

class SendMailMixin:
    def send_mail(self, form):
        addresses = [x.strip() for x in self.to_address.split(',')]
        if not self.from_address:
            if hasattr(settings, 'WAGTAILADMIN_NOTIFICATION_FROM_EMAIL'):
                self.from_address = settings.WAGTAILADMIN_NOTIFICATION_FROM_EMAIL
            elif hasattr(settings, 'DEFAULT_FROM_EMAIL'):
                self.from_address = settings.DEFAULT_FROM_EMAIL
            else:
                self.from_address = 'webmaster@localhost'
        content = []
        for field in form:
            value = field.value()
            if isinstance(value, list):
                value = ', '.join(value)
            content.append('{}: {}'.format(field.label, value))
        content = '\n'.join(content)
        email = EmailMessage(
            self.subject,
            content,
            self.from_address,
            addresses,
            [],
            reply_to=[form.cleaned_data['email']] if form.cleaned_data.get('email', False) else None,
        )
        email.send()

    class Meta:
        abstract = True
