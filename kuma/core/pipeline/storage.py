from __future__ import unicode_literals

from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from pipeline.storage import PipelineMixin


class ManifestPipelineStorage(PipelineMixin, ManifestStaticFilesStorage):
    pass
