from __future__ import unicode_literals

from attachments.models import Attachment
from django.contrib.contenttypes.admin import GenericStackedInline

class AttachmentInlines(GenericStackedInline):
    model = Attachment
    exclude = ()
    extra = 1

class AttachmentInlinesWithoutUser(AttachmentInlines):
	exclude = ("creator",)

class ModelWithAttachments():
	inlines = (AttachmentInlinesWithoutUser,)

	def save_formset(self, request, form, formset, change):
		instances = formset.save(commit=False)
		for instance in instances:
			instance.creator = request.user
			instance.save()
		formset.save_m2m()
