# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RestorableMongodbCollectionPropertiesResource(Model):
    """RestorableMongodbCollectionPropertiesResource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar _rid: A system generated property. A unique identifier.
    :vartype _rid: str
    :ivar operation_type: The operation type of this collection event.
     Possible values include: 'Create', 'Replace', 'Delete', 'SystemOperation'
    :vartype operation_type: str or ~azure.mgmt.cosmosdb.models.OperationType
    :ivar event_timestamp: The timestamp of this collection event.
    :vartype event_timestamp: str
    :ivar owner_id: The name of this restorable MongoDB collection.
    :vartype owner_id: str
    :ivar owner_resource_id: The resource Id of this restorable MongoDB
     collection.
    :vartype owner_resource_id: str
    """

    _validation = {
        '_rid': {'readonly': True},
        'operation_type': {'readonly': True},
        'event_timestamp': {'readonly': True},
        'owner_id': {'readonly': True},
        'owner_resource_id': {'readonly': True},
    }

    _attribute_map = {
        '_rid': {'key': '_rid', 'type': 'str'},
        'operation_type': {'key': 'operationType', 'type': 'str'},
        'event_timestamp': {'key': 'eventTimestamp', 'type': 'str'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'owner_resource_id': {'key': 'ownerResourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RestorableMongodbCollectionPropertiesResource, self).__init__(**kwargs)
        self._rid = None
        self.operation_type = None
        self.event_timestamp = None
        self.owner_id = None
        self.owner_resource_id = None
