# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema


__all__ = ["NasFlexcacheOriginSvm", "NasFlexcacheOriginSvmSchema"]
__pdoc__ = {
    "NasFlexcacheOriginSvmSchema.resource": False,
    "NasFlexcacheOriginSvm": False,
}


class NasFlexcacheOriginSvmSchema(ResourceSchema):
    """The fields of the NasFlexcacheOriginSvm object"""

    name = fields.Str(data_key="name")
    r""" Name of the source SVM. """

    @property
    def resource(self):
        return NasFlexcacheOriginSvm

    @property
    def patchable_fields(self):
        return [
        ]

    @property
    def postable_fields(self):
        return [
            "name",
        ]


class NasFlexcacheOriginSvm(Resource):  # pylint: disable=missing-docstring

    _schema = NasFlexcacheOriginSvmSchema