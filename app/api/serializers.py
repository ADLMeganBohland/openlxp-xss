import logging

from core.models import SchemaLedger, TransformationLedger
from rest_framework import serializers

logger = logging.getLogger('dict_config_logger')


class SchemaLedgerSerializer(serializers.ModelSerializer):
    """Serializes the SchemaLedger Model"""

    class Meta:
        model = SchemaLedger

        exclude = ('schema_file', 'major_version', 'minor_version',
                   'patch_version',)


class TransformationLedgerSerializer(serializers.ModelSerializer):
    """Serializes the SchemaLedger Model"""

    class Meta:
        model = TransformationLedger

        exclude = ('schema_mapping_file', 'source_schema', 'target_schema',)
