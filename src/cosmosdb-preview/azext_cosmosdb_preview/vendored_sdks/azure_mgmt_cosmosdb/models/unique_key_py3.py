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


class UniqueKey(Model):
    """The unique key on that enforces uniqueness constraint on documents in the
    collection in the Azure Cosmos DB service.

    :param paths: List of paths must be unique for each document in the Azure
     Cosmos DB service
    :type paths: list[str]
    """

    _attribute_map = {
        'paths': {'key': 'paths', 'type': '[str]'},
    }

    def __init__(self, *, paths=None, **kwargs) -> None:
        super(UniqueKey, self).__init__(**kwargs)
        self.paths = paths
